#!/bin/bash

name=$(pwd | sed -r 's/^.+\///')
IMAGE_TAG=hub.dev.laningtech.net/apps/${name}
PROJECT=project_face

optstring=":p:t:"

while getopts ${optstring} arg; do
  case ${arg} in
  p)
    echo "${OPTARG}"
    PROJECT="${OPTARG}"
    ;;
  t)
    echo "${OPTARG}"
    IMAGE_TAG="${OPTARG}"
    ;;
  esac
done

docker build -f docker/Dockerfile -t "${IMAGE_TAG}" \
  --build-arg AUTHORITYAPI_URL="http://admin.dev.laningtech.net/authorityapi/keypair/get_key/${PROJECT}/python" .
