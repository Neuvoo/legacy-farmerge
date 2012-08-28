#!/bin/bash

cd "$(dirname $0)"
protoc -I=. --python_out=. scheduler_status.proto
