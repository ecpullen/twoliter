ARG SDK
FROM $SDK
COPY build/rpms/ /twoliter/alpha/build/rpms/
COPY sbkeys/generate-local-sbkeys /twoliter/alpha/sbkeys/generate-local-sbkeys
COPY sbkeys/generate-aws-sbkeys /twoliter/alpha/sbkeys/generate-aws-sbkeys
COPY sources/models/src/variant /twoliter/alpha/sources/models/src/variant