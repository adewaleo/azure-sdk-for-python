# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from enum import Enum


class ImportMode(str, Enum):

    no_force = "NoForce"
    force = "Force"


class SkuName(str, Enum):

    classic = "Classic"
    basic = "Basic"
    standard = "Standard"
    premium = "Premium"


class SkuTier(str, Enum):

    classic = "Classic"
    basic = "Basic"
    standard = "Standard"
    premium = "Premium"


class ProvisioningState(str, Enum):

    creating = "Creating"
    updating = "Updating"
    deleting = "Deleting"
    succeeded = "Succeeded"
    failed = "Failed"
    canceled = "Canceled"


class DefaultAction(str, Enum):

    allow = "Allow"
    deny = "Deny"


class Action(str, Enum):

    allow = "Allow"


class PolicyStatus(str, Enum):

    enabled = "enabled"
    disabled = "disabled"


class TrustPolicyType(str, Enum):

    notary = "Notary"


class PasswordName(str, Enum):

    password = "password"
    password2 = "password2"


class RegistryUsageUnit(str, Enum):

    count = "Count"
    bytes = "Bytes"


class WebhookStatus(str, Enum):

    enabled = "enabled"
    disabled = "disabled"


class WebhookAction(str, Enum):

    push = "push"
    delete = "delete"
    quarantine = "quarantine"
    chart_push = "chart_push"
    chart_delete = "chart_delete"


class CreatedByType(str, Enum):

    user = "User"
    application = "Application"
    managed_identity = "ManagedIdentity"
    key = "Key"


class OS(str, Enum):

    windows = "Windows"
    linux = "Linux"


class RunStatus(str, Enum):

    queued = "Queued"
    started = "Started"
    running = "Running"
    succeeded = "Succeeded"
    failed = "Failed"
    canceled = "Canceled"
    error = "Error"
    timeout = "Timeout"


class RunType(str, Enum):

    quick_build = "QuickBuild"
    quick_run = "QuickRun"
    auto_build = "AutoBuild"
    auto_run = "AutoRun"


class Architecture(str, Enum):

    amd64 = "amd64"
    x86 = "x86"
    three_eight_six = "386"
    arm = "arm"
    arm64 = "arm64"


class Variant(str, Enum):

    v6 = "v6"
    v7 = "v7"
    v8 = "v8"


class ResourceIdentityType(str, Enum):

    system_assigned = "SystemAssigned"
    user_assigned = "UserAssigned"
    system_assigned_user_assigned = "SystemAssigned, UserAssigned"
    none = "None"


class TaskStatus(str, Enum):

    disabled = "Disabled"
    enabled = "Enabled"


class BaseImageDependencyType(str, Enum):

    build_time = "BuildTime"
    run_time = "RunTime"


class TriggerStatus(str, Enum):

    disabled = "Disabled"
    enabled = "Enabled"


class SourceControlType(str, Enum):

    github = "Github"
    visual_studio_team_service = "VisualStudioTeamService"


class TokenType(str, Enum):

    pat = "PAT"
    oauth = "OAuth"


class SourceTriggerEvent(str, Enum):

    commit = "commit"
    pullrequest = "pullrequest"


class BaseImageTriggerType(str, Enum):

    all = "All"
    runtime = "Runtime"


class UpdateTriggerPayloadType(str, Enum):

    default = "Default"
    token = "Token"


class SourceRegistryLoginMode(str, Enum):

    none = "None"
    default = "Default"


class SecretObjectType(str, Enum):

    opaque = "Opaque"
    vaultsecret = "Vaultsecret"


class TokenCertificateName(str, Enum):

    certificate1 = "certificate1"
    certificate2 = "certificate2"


class TokenPasswordName(str, Enum):

    password1 = "password1"
    password2 = "password2"


class TokenStatus(str, Enum):

    enabled = "enabled"
    disabled = "disabled"
