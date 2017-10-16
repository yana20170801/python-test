#!/bin/bash

echo ${DEPLOY_TYPE}
echo ${DEPLOY_K}
echo ${_TEST_ACCOUNT}

cat test.json | jq '.url'