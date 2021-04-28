#!/bin/bash

# Log the given message at the given level. All logs are written to stderr with a timestamp.
function log() {
    local -r level="$1"
    local -r message="$2"
    local -r timestamp=$(date +"%Y-%m-%d %H:%M:%S")
    local -r script_name="$(basename "$0")"
    echo >&2 -e "${timestamp} [${level}] [$script_name] ${message}"
}

# Log the given message at INFO level. All logs are written to stderr with a timestamp.
function log_info() {
    local -r message="$1"
    log "\033[1mINFO\033[0m" "$message"
}

# Log the given message at WARN level. All logs are written to stderr with a timestamp.
function log_warn() {
    local -r message="$1"
    log "\033[33;1mWARN\033[0m" "$message"
}

# Log the given message at ERROR level. All logs are written to stderr with a timestamp.
function log_error() {
    local -r message="$1"
    log "\033[31;1mERROR\033[0m" "$message"
}
