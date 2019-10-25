import asyncio
import logging
import os
from azure.eventhub.aio import EventHubConsumerClient
from azure.eventhub.aio import FileBasedPartitionManager

RETRY_TOTAL = 3  # max number of retries for receive operations within the receive timeout. Actual number of retries clould be less if RECEIVE_TIMEOUT is too small
CONNECTION_STR = os.environ["EVENT_HUB_CONN_STR"]

logging.basicConfig(level=logging.INFO)


async def do_operation(event):
    # do some sync or async operations. If the operation is i/o intensive, async will have better performance
    print(event)


async def process_events(partition_context, events):
    if events:
        await asyncio.gather(*[do_operation(event) for event in events])
        await partition_context.update_checkpoint(events[-1])
    else:
        print("empty events received", "partition:", partition_context.partition_id)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    partition_manager = FileBasedPartitionManager("consumer_pm_store")
    client = EventHubConsumerClient.from_connection_string(
        CONNECTION_STR,
        partition_manager=partition_manager,  # For load balancing and checkpointing. Leave None for no load balancing
        retry_total=RETRY_TOTAL  # num of retry times if receiving from EventHub has an error.
    )
    try:
        loop.run_until_complete(
            client.receive(process_events, consumer_group="$default")
        )
    except KeyboardInterrupt:
        loop.run_until_complete(client.close())
    finally:
        loop.stop()
