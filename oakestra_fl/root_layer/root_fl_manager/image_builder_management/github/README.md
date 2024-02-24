### Note
The contents of this "github" folder are a builder image that can build images (fl client envs).

Because this image is "static", i.e. it will build the envs based on the provided custom (repo-specific) CMD, it is hosted on github's package/container registry (ghcr.io).

The source code is located here because it is lightweight to store and it is located next to the place that uses it the most.

I.e. the code in this github folder is not invoked by the other Oakestra code. It is standalone.
It is kept here for transparancy, usability, and readability, instead of its own (sub)repo.
