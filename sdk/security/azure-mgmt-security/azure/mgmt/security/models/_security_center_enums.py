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


class AadConnectivityStateEnum(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The connectivity state of the external AAD solution
    """

    DISCOVERED = "Discovered"
    NOT_LICENSED = "NotLicensed"
    CONNECTED = "Connected"

class ActionType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The type of the action that will be triggered by the Automation
    """

    LOGIC_APP = "LogicApp"
    EVENT_HUB = "EventHub"
    WORKSPACE = "Workspace"

class AdaptiveApplicationControlIssue(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """An alert that machines within a group can have
    """

    VIOLATIONS_AUDITED = "ViolationsAudited"
    VIOLATIONS_BLOCKED = "ViolationsBlocked"
    MSI_AND_SCRIPT_VIOLATIONS_AUDITED = "MsiAndScriptViolationsAudited"
    MSI_AND_SCRIPT_VIOLATIONS_BLOCKED = "MsiAndScriptViolationsBlocked"
    EXECUTABLE_VIOLATIONS_AUDITED = "ExecutableViolationsAudited"
    RULES_VIOLATED_MANUALLY = "RulesViolatedManually"

class AdditionalWorkspaceDataType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Data types sent to workspace.
    """

    ALERTS = "Alerts"
    RAW_EVENTS = "RawEvents"

class AdditionalWorkspaceType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Workspace type.
    """

    SENTINEL = "Sentinel"

class AlertNotifications(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Whether to send security alerts notifications to the security contact
    """

    #: Get notifications on new alerts.
    ON = "On"
    #: Don't get notifications on new alerts.
    OFF = "Off"

class AlertSeverity(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The risk level of the threat that was detected. Learn more:
    https://docs.microsoft.com/en-us/azure/security-center/security-center-alerts-overview#how-are-alerts-classified.
    """

    #: Informational.
    INFORMATIONAL = "Informational"
    #: Low.
    LOW = "Low"
    #: Medium.
    MEDIUM = "Medium"
    #: High.
    HIGH = "High"

class AlertStatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The life cycle status of the alert.
    """

    #: An alert which doesn't specify a value is assigned the status 'Active'.
    ACTIVE = "Active"
    #: Alert closed after handling.
    RESOLVED = "Resolved"
    #: Alert dismissed as false positive.
    DISMISSED = "Dismissed"

class AlertsToAdmins(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Whether to send security alerts notifications to subscription admins
    """

    #: Send notification on new alerts to the subscription's admins.
    ON = "On"
    #: Don't send notification on new alerts to the subscription's admins.
    OFF = "Off"

class AssessedResourceType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Sub-assessment resource type
    """

    SQL_SERVER_VULNERABILITY = "SqlServerVulnerability"
    CONTAINER_REGISTRY_VULNERABILITY = "ContainerRegistryVulnerability"
    SERVER_VULNERABILITY = "ServerVulnerability"

class AssessmentStatusCode(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Programmatic code for the status of the assessment
    """

    #: The resource is healthy.
    HEALTHY = "Healthy"
    #: The resource has a security issue that needs to be addressed.
    UNHEALTHY = "Unhealthy"
    #: Assessment for this resource did not happen.
    NOT_APPLICABLE = "NotApplicable"

class AssessmentType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """BuiltIn if the assessment based on built-in Azure Policy definition, Custom if the assessment
    based on custom Azure Policy definition
    """

    #: Azure Security Center managed assessments.
    BUILT_IN = "BuiltIn"
    #: User defined policies that are automatically ingested from Azure Policy to Azure Security
    #: Center.
    CUSTOM_POLICY = "CustomPolicy"
    #: User assessments pushed directly by the user or other third party to Azure Security Center.
    CUSTOMER_MANAGED = "CustomerManaged"
    #: An assessment that was created by a verified 3rd party if the user connected it to ASC.
    VERIFIED_PARTNER = "VerifiedPartner"

class AuthenticationProvisioningState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """State of the multi-cloud connector
    """

    #: Valid connector.
    VALID = "Valid"
    #: Invalid connector.
    INVALID = "Invalid"
    #: the connection has expired.
    EXPIRED = "Expired"
    #: Incorrect policy of the connector.
    INCORRECT_POLICY = "IncorrectPolicy"

class AuthenticationType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Connect to your cloud account, for AWS use either account credentials or role-based
    authentication. For GCP use account organization credentials.
    """

    #: AWS cloud account connector user credentials authentication.
    AWS_CREDS = "awsCreds"
    #: AWS account connector assume role authentication.
    AWS_ASSUME_ROLE = "awsAssumeRole"
    #: GCP account connector service to service authentication.
    GCP_CREDENTIALS = "gcpCredentials"

class AutoProvision(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Describes what kind of security agent provisioning action to take
    """

    #: Install missing security agent on VMs automatically.
    ON = "On"
    #: Do not install security agent on the VMs automatically.
    OFF = "Off"

class BundleType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Alert Simulator supported bundles.
    """

    APP_SERVICES = "AppServices"
    DNS = "DNS"
    KEY_VAULTS = "KeyVaults"
    KUBERNETES_SERVICE = "KubernetesService"
    RESOURCE_MANAGER = "ResourceManager"
    SQL_SERVERS = "SqlServers"
    STORAGE_ACCOUNTS = "StorageAccounts"
    VIRTUAL_MACHINES = "VirtualMachines"

class Categories(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The categories of resource that is at risk when the assessment is unhealthy
    """

    COMPUTE = "Compute"
    NETWORKING = "Networking"
    DATA = "Data"
    IDENTITY_AND_ACCESS = "IdentityAndAccess"
    IO_T = "IoT"

class ConfigurationStatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The configuration status of the machines group or machine or rule
    """

    CONFIGURED = "Configured"
    NOT_CONFIGURED = "NotConfigured"
    IN_PROGRESS = "InProgress"
    FAILED = "Failed"
    NO_STATUS = "NoStatus"

class ConnectionType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    INTERNAL = "Internal"
    EXTERNAL = "External"

class ControlType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The type of security control (for example, BuiltIn)
    """

    #: Azure Security Center managed assessments.
    BUILT_IN = "BuiltIn"
    #: Non Azure Security Center managed assessments.
    CUSTOM = "Custom"

class CreatedByType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The type of identity that created the resource.
    """

    USER = "User"
    APPLICATION = "Application"
    MANAGED_IDENTITY = "ManagedIdentity"
    KEY = "Key"

class DataSource(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    #: Devices twin data.
    TWIN_DATA = "TwinData"

class Direction(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The rule's direction
    """

    INBOUND = "Inbound"
    OUTBOUND = "Outbound"

class EndOfSupportStatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """End of support status.
    """

    NONE = "None"
    NO_LONGER_SUPPORTED = "noLongerSupported"
    VERSION_NO_LONGER_SUPPORTED = "versionNoLongerSupported"
    UPCOMING_NO_LONGER_SUPPORTED = "upcomingNoLongerSupported"
    UPCOMING_VERSION_NO_LONGER_SUPPORTED = "upcomingVersionNoLongerSupported"

class EnforcementMode(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The application control policy enforcement/protection mode of the machine group
    """

    AUDIT = "Audit"
    ENFORCE = "Enforce"
    NONE = "None"

class EnforcementSupport(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The machine supportability of Enforce feature
    """

    SUPPORTED = "Supported"
    NOT_SUPPORTED = "NotSupported"
    UNKNOWN = "Unknown"

class Enum13(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    ACTIVATE = "Activate"
    DISMISS = "Dismiss"
    START = "Start"
    RESOLVE = "Resolve"
    CLOSE = "Close"

class Enum15(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    EFFECTIVE = "effective"
    CUSTOM = "custom"

class Enum69(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    MCAS = "MCAS"
    WDATP = "WDATP"
    WDATP_EXCLUDE_LINUX_PUBLIC_PREVIEW = "WDATP_EXCLUDE_LINUX_PUBLIC_PREVIEW"
    SENTINEL = "Sentinel"

class EventSource(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """A valid event source type.
    """

    ASSESSMENTS = "Assessments"
    SUB_ASSESSMENTS = "SubAssessments"
    ALERTS = "Alerts"
    SECURE_SCORES = "SecureScores"
    SECURE_SCORES_SNAPSHOT = "SecureScoresSnapshot"
    SECURE_SCORE_CONTROLS = "SecureScoreControls"
    SECURE_SCORE_CONTROLS_SNAPSHOT = "SecureScoreControlsSnapshot"
    REGULATORY_COMPLIANCE_ASSESSMENT = "RegulatoryComplianceAssessment"
    REGULATORY_COMPLIANCE_ASSESSMENT_SNAPSHOT = "RegulatoryComplianceAssessmentSnapshot"

class ExpandControlsEnum(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    #: Add definition object for each control.
    DEFINITION = "definition"

class ExpandEnum(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    #: All links associated with an assessment.
    LINKS = "links"
    #: Assessment metadata.
    METADATA = "metadata"

class ExportData(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    #: Agent raw events.
    RAW_EVENTS = "RawEvents"

class ExternalSecuritySolutionKindEnum(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The kind of the external solution
    """

    CEF = "CEF"
    ATA = "ATA"
    AAD = "AAD"

class FileType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The type of the file (for Linux files - Executable is used)
    """

    EXE = "Exe"
    DLL = "Dll"
    MSI = "Msi"
    SCRIPT = "Script"
    EXECUTABLE = "Executable"
    UNKNOWN = "Unknown"

class HybridComputeProvisioningState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """State of the service principal and its secret
    """

    #: Valid service principal details.
    VALID = "Valid"
    #: Invalid service principal details.
    INVALID = "Invalid"
    #: the service principal details are expired.
    EXPIRED = "Expired"

class ImplementationEffort(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The implementation effort required to remediate this assessment
    """

    LOW = "Low"
    MODERATE = "Moderate"
    HIGH = "High"

class Intent(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The kill chain related intent behind the alert. For list of supported values, and explanations
    of Azure Security Center's supported kill chain intents.
    """

    #: Unknown.
    UNKNOWN = "Unknown"
    #: PreAttack could be either an attempt to access a certain resource regardless of a malicious
    #: intent, or a failed attempt to gain access to a target system to gather information prior to
    #: exploitation. This step is usually detected as an attempt, originating from outside the
    #: network, to scan the target system and find a way in.  Further details on the PreAttack stage
    #: can be read in `MITRE Pre-Att&ck matrix <https://attack.mitre.org/matrices/pre/>`_.
    PRE_ATTACK = "PreAttack"
    #: InitialAccess is the stage where an attacker manages to get foothold on the attacked resource.
    INITIAL_ACCESS = "InitialAccess"
    #: Persistence is any access, action, or configuration change to a system that gives a threat
    #: actor a persistent presence on that system.
    PERSISTENCE = "Persistence"
    #: Privilege escalation is the result of actions that allow an adversary to obtain a higher level
    #: of permissions on a system or network.
    PRIVILEGE_ESCALATION = "PrivilegeEscalation"
    #: Defense evasion consists of techniques an adversary may use to evade detection or avoid other
    #: defenses.
    DEFENSE_EVASION = "DefenseEvasion"
    #: Credential access represents techniques resulting in access to or control over system, domain,
    #: or service credentials that are used within an enterprise environment.
    CREDENTIAL_ACCESS = "CredentialAccess"
    #: Discovery consists of techniques that allow the adversary to gain knowledge about the system
    #: and internal network.
    DISCOVERY = "Discovery"
    #: Lateral movement consists of techniques that enable an adversary to access and control remote
    #: systems on a network and could, but does not necessarily, include execution of tools on remote
    #: systems.
    LATERAL_MOVEMENT = "LateralMovement"
    #: The execution tactic represents techniques that result in execution of adversary-controlled
    #: code on a local or remote system.
    EXECUTION = "Execution"
    #: Collection consists of techniques used to identify and gather information, such as sensitive
    #: files, from a target network prior to exfiltration.
    COLLECTION = "Collection"
    #: Exfiltration refers to techniques and attributes that result or aid in the adversary removing
    #: files and information from a target network.
    EXFILTRATION = "Exfiltration"
    #: The command and control tactic represents how adversaries communicate with systems under their
    #: control within a target network.
    COMMAND_AND_CONTROL = "CommandAndControl"
    #: Impact events primarily try to directly reduce the availability or integrity of a system,
    #: service, or network; including manipulation of data to impact a business or operational
    #: process.
    IMPACT = "Impact"
    #: Probing could be either an attempt to access a certain resource regardless of a malicious
    #: intent, or a failed attempt to gain access to a target system to gather information prior to
    #: exploitation.
    PROBING = "Probing"
    #: Exploitation is the stage where an attacker manages to get a foothold on the attacked resource.
    #: This stage is relevant for compute hosts and resources such as user accounts, certificates etc.
    EXPLOITATION = "Exploitation"

class KindEnum(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The kind of alert simulation.
    """

    #: Simulate alerts according to bundles.
    BUNDLES = "Bundles"

class Operator(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """A valid comparer operator to use. A case-insensitive comparison will be applied for String
    PropertyType.
    """

    #: Applies for decimal and non-decimal operands.
    EQUALS = "Equals"
    #: Applies only for decimal operands.
    GREATER_THAN = "GreaterThan"
    #: Applies only for decimal operands.
    GREATER_THAN_OR_EQUAL_TO = "GreaterThanOrEqualTo"
    #: Applies only for decimal operands.
    LESSER_THAN = "LesserThan"
    #: Applies only for decimal operands.
    LESSER_THAN_OR_EQUAL_TO = "LesserThanOrEqualTo"
    #: Applies  for decimal and non-decimal operands.
    NOT_EQUALS = "NotEquals"
    #: Applies only for non-decimal operands.
    CONTAINS = "Contains"
    #: Applies only for non-decimal operands.
    STARTS_WITH = "StartsWith"
    #: Applies only for non-decimal operands.
    ENDS_WITH = "EndsWith"

class PermissionProperty(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """A permission detected in the cloud account.
    """

    #: This permission provides read only access to AWS Security Hub resources.
    AWS_AWS_SECURITY_HUB_READ_ONLY_ACCESS = "AWS::AWSSecurityHubReadOnlyAccess"
    #: This permission grants access to read security configuration metadata.
    AWS_SECURITY_AUDIT = "AWS::SecurityAudit"
    #: The permission provides for EC2 Automation service to execute activities defined within
    #: Automation documents.
    AWS_AMAZON_SSM_AUTOMATION_ROLE = "AWS::AmazonSSMAutomationRole"
    #: This permission provides read only access to GCP Security Command Center.
    GCP_SECURITY_CENTER_ADMIN_VIEWER = "GCP::Security Center Admin Viewer"

class PricingTier(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The pricing tier value. Azure Security Center is provided in two pricing tiers: free and
    standard, with the standard tier available with a trial period. The standard tier offers
    advanced security capabilities, while the free tier offers basic security features.
    """

    #: Get free Azure security center experience with basic security features.
    FREE = "Free"
    #: Get the standard Azure security center experience with advanced security features.
    STANDARD = "Standard"

class PropertyType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The data type of the compared operands (string, integer, floating point number or a boolean
    [true/false]]
    """

    STRING = "String"
    INTEGER = "Integer"
    NUMBER = "Number"
    BOOLEAN = "Boolean"

class ProtocolEnum(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    TCP = "TCP"
    UDP = "UDP"
    ALL = "*"

class ProvisioningState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The security family provisioning State
    """

    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    UPDATING = "Updating"

class Rank(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The rank of the sensitivity label.
    """

    NONE = "None"
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"
    CRITICAL = "Critical"

class RecommendationAction(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The recommendation action of the machine or rule
    """

    RECOMMENDED = "Recommended"
    ADD = "Add"
    REMOVE = "Remove"

class RecommendationConfigStatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Recommendation status. When the recommendation status is disabled recommendations are not
    generated.
    """

    DISABLED = "Disabled"
    ENABLED = "Enabled"

class RecommendationStatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The initial recommendation status of the machine group or machine
    """

    RECOMMENDED = "Recommended"
    NOT_RECOMMENDED = "NotRecommended"
    NOT_AVAILABLE = "NotAvailable"
    NO_STATUS = "NoStatus"

class RecommendationType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The type of IoT Security recommendation.
    """

    #: Authentication schema used for pull an edge module from an ACR repository does not use Service
    #: Principal Authentication.
    IO_T_ACRAUTHENTICATION = "IoT_ACRAuthentication"
    #: IoT agent message size capacity is currently underutilized, causing an increase in the number
    #: of sent messages. Adjust message intervals for better utilization.
    IO_T_AGENT_SENDS_UNUTILIZED_MESSAGES = "IoT_AgentSendsUnutilizedMessages"
    #: Identified security related system configuration issues.
    IO_T_BASELINE = "IoT_Baseline"
    #: You can optimize Edge Hub memory usage by turning off protocol heads for any protocols not used
    #: by Edge modules in your solution.
    IO_T_EDGE_HUB_MEM_OPTIMIZE = "IoT_EdgeHubMemOptimize"
    #: Logging is disabled for this edge module.
    IO_T_EDGE_LOGGING_OPTIONS = "IoT_EdgeLoggingOptions"
    #: A minority within a device security group has inconsistent Edge Module settings with the rest
    #: of their group.
    IO_T_INCONSISTENT_MODULE_SETTINGS = "IoT_InconsistentModuleSettings"
    #: Install the Azure Security of Things Agent.
    IO_T_INSTALL_AGENT = "IoT_InstallAgent"
    #: IP Filter Configuration should have rules defined for allowed traffic and should deny all other
    #: traffic by default.
    IO_T_IPFILTER_DENY_ALL = "IoT_IPFilter_DenyAll"
    #: An Allow IP Filter rules source IP range is too large. Overly permissive rules might expose
    #: your IoT hub to malicious intenders.
    IO_T_IPFILTER_PERMISSIVE_RULE = "IoT_IPFilter_PermissiveRule"
    #: A listening endpoint was found on the device.
    IO_T_OPEN_PORTS = "IoT_OpenPorts"
    #: An Allowed firewall policy was found (INPUT/OUTPUT). The policy should Deny all traffic by
    #: default and define rules to allow necessary communication to/from the device.
    IO_T_PERMISSIVE_FIREWALL_POLICY = "IoT_PermissiveFirewallPolicy"
    #: A rule in the firewall has been found that contains a permissive pattern for a wide range of IP
    #: addresses or Ports.
    IO_T_PERMISSIVE_INPUT_FIREWALL_RULES = "IoT_PermissiveInputFirewallRules"
    #: A rule in the firewall has been found that contains a permissive pattern for a wide range of IP
    #: addresses or Ports.
    IO_T_PERMISSIVE_OUTPUT_FIREWALL_RULES = "IoT_PermissiveOutputFirewallRules"
    #: Edge module is configured to run in privileged mode, with extensive Linux capabilities or with
    #: host-level network access (send/receive data to host machine).
    IO_T_PRIVILEGED_DOCKER_OPTIONS = "IoT_PrivilegedDockerOptions"
    #: Same authentication credentials to the IoT Hub used by multiple devices. This could indicate an
    #: illegitimate device impersonating a legitimate device. It also exposes the risk of device
    #: impersonation by an attacker.
    IO_T_SHARED_CREDENTIALS = "IoT_SharedCredentials"
    #: Insecure TLS configurations detected. Immediate upgrade recommended.
    IO_T_VULNERABLE_TLS_CIPHER_SUITE = "IoT_VulnerableTLSCipherSuite"

class ReportedSeverity(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Assessed alert severity.
    """

    INFORMATIONAL = "Informational"
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"

class ResourceIdentifierType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """There can be multiple identifiers of different type per alert, this field specify the
    identifier type.
    """

    AZURE_RESOURCE = "AzureResource"
    LOG_ANALYTICS = "LogAnalytics"

class ResourceStatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The status of the resource regarding a single assessment
    """

    #: This assessment on the resource is healthy.
    HEALTHY = "Healthy"
    #: This assessment is not applicable to this resource.
    NOT_APPLICABLE = "NotApplicable"
    #: This assessment is turned off by policy on this subscription.
    OFF_BY_POLICY = "OffByPolicy"
    #: This assessment on the resource is not healthy.
    NOT_HEALTHY = "NotHealthy"

class RuleSeverity(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The rule severity.
    """

    #: High.
    HIGH = "High"
    #: Medium.
    MEDIUM = "Medium"
    #: Low.
    LOW = "Low"
    #: Informational.
    INFORMATIONAL = "Informational"
    #: Obsolete.
    OBSOLETE = "Obsolete"

class RuleState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Possible states of the rule
    """

    ENABLED = "Enabled"
    DISABLED = "Disabled"
    EXPIRED = "Expired"

class RuleStatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The rule result status.
    """

    #: NonFinding.
    NON_FINDING = "NonFinding"
    #: Finding.
    FINDING = "Finding"
    #: InternalError.
    INTERNAL_ERROR = "InternalError"

class RuleType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The rule type.
    """

    #: Binary.
    BINARY = "Binary"
    #: BaselineExpected.
    BASELINE_EXPECTED = "BaselineExpected"
    #: PositiveList.
    POSITIVE_LIST = "PositiveList"
    #: NegativeList.
    NEGATIVE_LIST = "NegativeList"

class ScanState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The scan status.
    """

    #: Failed.
    FAILED = "Failed"
    #: FailedToRun.
    FAILED_TO_RUN = "FailedToRun"
    #: InProgress.
    IN_PROGRESS = "InProgress"
    #: Passed.
    PASSED = "Passed"

class ScanTriggerType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The scan trigger type.
    """

    #: OnDemand.
    ON_DEMAND = "OnDemand"
    #: Recurring.
    RECURRING = "Recurring"

class SecurityFamily(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The security family of the discovered solution
    """

    WAF = "Waf"
    NGFW = "Ngfw"
    SAAS_WAF = "SaasWaf"
    VA = "Va"

class SecuritySolutionStatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Status of the IoT Security solution.
    """

    ENABLED = "Enabled"
    DISABLED = "Disabled"

class ServerVulnerabilityAssessmentPropertiesProvisioningState(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The provisioningState of the vulnerability assessment capability on the VM
    """

    SUCCEEDED = "Succeeded"
    FAILED = "Failed"
    CANCELED = "Canceled"
    PROVISIONING = "Provisioning"
    DEPROVISIONING = "Deprovisioning"

class SettingKind(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """the kind of the settings string
    """

    DATA_EXPORT_SETTINGS = "DataExportSettings"
    ALERT_SUPPRESSION_SETTING = "AlertSuppressionSetting"
    ALERT_SYNC_SETTINGS = "AlertSyncSettings"

class Severity(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The sub-assessment severity level
    """

    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"

class Source(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The platform where the assessed resource resides
    """

    #: Resource is in Azure.
    AZURE = "Azure"
    #: Resource in an on premise machine connected to Azure cloud.
    ON_PREMISE = "OnPremise"
    #: SQL Resource in an on premise machine connected to Azure cloud.
    ON_PREMISE_SQL = "OnPremiseSql"

class SourceSystem(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The source type of the machine group
    """

    AZURE_APP_LOCKER = "Azure_AppLocker"
    AZURE_AUDIT_D = "Azure_AuditD"
    NON_AZURE_APP_LOCKER = "NonAzure_AppLocker"
    NON_AZURE_AUDIT_D = "NonAzure_AuditD"
    NONE = "None"

class State(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Aggregative state based on the standard's supported controls states
    """

    #: All supported regulatory compliance controls in the given standard have a passed state.
    PASSED = "Passed"
    #: At least one supported regulatory compliance control in the given standard has a state of
    #: failed.
    FAILED = "Failed"
    #: All supported regulatory compliance controls in the given standard have a state of skipped.
    SKIPPED = "Skipped"
    #: No supported regulatory compliance data for the given standard.
    UNSUPPORTED = "Unsupported"

class Status(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The status of the port
    """

    REVOKED = "Revoked"
    INITIATED = "Initiated"

class StatusReason(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """A description of why the ``status`` has its value
    """

    EXPIRED = "Expired"
    USER_REQUESTED = "UserRequested"
    NEWER_REQUEST_INITIATED = "NewerRequestInitiated"

class SubAssessmentStatusCode(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Programmatic code for the status of the assessment
    """

    #: The resource is healthy.
    HEALTHY = "Healthy"
    #: The resource has a security issue that needs to be addressed.
    UNHEALTHY = "Unhealthy"
    #: Assessment for this resource did not happen.
    NOT_APPLICABLE = "NotApplicable"

class Threats(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Threats impact of the assessment
    """

    ACCOUNT_BREACH = "accountBreach"
    DATA_EXFILTRATION = "dataExfiltration"
    DATA_SPILLAGE = "dataSpillage"
    MALICIOUS_INSIDER = "maliciousInsider"
    ELEVATION_OF_PRIVILEGE = "elevationOfPrivilege"
    THREAT_RESISTANCE = "threatResistance"
    MISSING_COVERAGE = "missingCoverage"
    DENIAL_OF_SERVICE = "denialOfService"

class TransportProtocol(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):

    TCP = "TCP"
    UDP = "UDP"

class UnmaskedIpLoggingStatus(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """Unmasked IP address logging status
    """

    #: Unmasked IP logging is disabled.
    DISABLED = "Disabled"
    #: Unmasked IP logging is enabled.
    ENABLED = "Enabled"

class UserImpact(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The user impact of the assessment
    """

    LOW = "Low"
    MODERATE = "Moderate"
    HIGH = "High"

class ValueType(with_metaclass(_CaseInsensitiveEnumMeta, str, Enum)):
    """The value type of the items in the list.
    """

    #: An IP range in CIDR format (e.g. '192.168.0.1/8').
    IP_CIDR = "IpCidr"
    #: Any string value.
    STRING = "String"
