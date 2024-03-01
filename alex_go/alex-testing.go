package main

import (
	"context"
	"fmt"
	"log"
	"time"

	"github.com/containerd/containerd"
	"github.com/containerd/containerd/cio"
	"github.com/containerd/containerd/namespaces"
	"github.com/containerd/containerd/oci"
)

func main() {
	// Create a new context with a timeout
	ctx, cancel := context.WithTimeout(context.Background(), 5*time.Minute)
	defer cancel()

	log.Printf("AAA")

	// Create a new containerd client
	client, err := containerd.New("/run/containerd/containerd.sock")
	if err != nil {
		log.Fatalf("failed to create client: %v", err)
	}
	defer client.Close()

	log.Printf("BBB")

	// Create a new namespace for the container
	//ctx = namespaces.WithNamespace(ctx, "alex")
	ctx = namespaces.WithNamespace(ctx, "alex")

	log.Printf("B11")

	// Define the container image
	image, err := client.Pull(ctx, "docker.io/library/hello-world:latest", containerd.WithPullUnpack)
	if err != nil {
		log.Fatalf("failed to pull image: %v", err)
	}

	log.Printf("CCC")

	// Create a container
	container, err := client.NewContainer(
		ctx,
		"hello-world",
		containerd.WithImage(image),
		containerd.WithNewSnapshot("hello-world-snapshot", image),
		containerd.WithNewSpec(oci.WithImageConfig(image)),
	)
	if err != nil {
		log.Fatalf("failed to create container: %v", err)
	}

	log.Printf("DDD")

	// Start the container
	task, err := container.NewTask(ctx, cio.NewCreator(cio.WithStdio))
	if err != nil {
		log.Fatalf("failed to create task: %v", err)
	}

	log.Printf("EEE")

	// Wait for the task to exit
	statusC, err := task.Wait(ctx)
	if err != nil {
		log.Fatalf("failed to wait on task: %v", err)
	}

	log.Printf("FFF")

	// Print the task status
	status := <-statusC
	code, _, _ := status.Result()
	fmt.Printf("hello-world exited with status: %d\n", code)
}
