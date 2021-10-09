# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum, EnumMeta
from six import with_metaclass

class _CaseInsensitiveEnumMeta(EnumMeta):
    def __getitem__(self, name):
        return super().__getitem__(name.upper())

    def __getattr__(cls, name):
        """Return the enum member matching `name`
        We use __getattr__ instead of descriptors or inserting into the enum
        class' __dict__ in order to support `name` and `value` being both
        properties for enum members (which live in the class' __dict__) and
        enum members themselves.
        """
        try:
            return cls._member_map_[name.upper()]
        except KeyError:
            raise AttributeError(name)


class CacheIdentityType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The type of identity used for the cache
    """

    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"
    SYSTEM_ASSIGNED_USER_ASSIGNED = "SystemAssigned, UserAssigned"
    NONE = "None"

class CreatedByType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The type of identity that created the resource.
    """

    USER = "User"
    APPLICATION = "Application"
    MANAGED_IDENTITY = "ManagedIdentity"
    KEY = "Key"

class DomainJoinedType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """True if the HPC Cache is joined to the Active Directory domain.
    """

    YES = "Yes"
    NO = "No"
    ERROR = "Error"

class FirmwareStatusType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """True if there is a firmware update ready to install on this Cache. The firmware will
    automatically be installed after firmwareUpdateDeadline if not triggered earlier via the
    upgrade operation.
    """

    AVAILABLE = "available"
    UNAVAILABLE = "unavailable"

class HealthStateType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """List of Cache health states.
    """

    UNKNOWN = "Unknown"
    HEALTHY = "Healthy"
    DEGRADED = "Degraded"
    DOWN = "Down"
    TRANSITIONING = "Transitioning"
    STOPPING = "Stopping"
    STOPPED = "Stopped"
    UPGRADING = "Upgrading"
    FLUSHING = "Flushing"

class MetricAggregationType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    NOT_SPECIFIED = "NotSpecified"
    NONE = "None"
    AVERAGE = "Average"
    MINIMUM = "Minimum"
    MAXIMUM = "Maximum"
    TOTAL = "Total"
    COUNT = "Count"

class NfsAccessRuleAccess(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Access allowed by this rule.
    """

    NO = "no"
    RO = "ro"
    RW = "rw"

class NfsAccessRuleScope(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Scope for this rule. The scope and filter determine which clients match the rule.
    """

    DEFAULT = "default"
    NETWORK = "network"
    HOST = "host"

class OperationalStateType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Storage target operational state.
    """

    READY = "Ready"
    BUSY = "Busy"
    SUSPENDED = "Suspended"
    FLUSHING = "Flushing"

class ProvisioningStateType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """ARM provisioning state, see
    https://github.com/Azure/azure-resource-manager-rpc/blob/master/v1.0/Addendum.md#provisioningstate-property
    """

    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CANCELLED = "Cancelled"
    CREATING = "Creating"
    DELETING = "Deleting"
    UPDATING = "Updating"

class ReasonCode(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The reason for the restriction. As of now this can be "QuotaId" or
    "NotAvailableForSubscription". "QuotaId" is set when the SKU has requiredQuotas parameter as
    the subscription does not belong to that quota. "NotAvailableForSubscription" is related to
    capacity at the datacenter.
    """

    QUOTA_ID = "QuotaId"
    NOT_AVAILABLE_FOR_SUBSCRIPTION = "NotAvailableForSubscription"

class StorageTargetType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Type of the Storage Target.
    """

    NFS3 = "nfs3"
    CLFS = "clfs"
    UNKNOWN = "unknown"
    BLOB_NFS = "blobNfs"

class UsernameDownloadedType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Indicates whether or not the HPC Cache has performed the username download successfully.
    """

    YES = "Yes"
    NO = "No"
    ERROR = "Error"

class UsernameSource(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """This setting determines how the cache gets username and group names for clients.
    """

    AD = "AD"
    LDAP = "LDAP"
    FILE = "File"
    NONE = "None"
