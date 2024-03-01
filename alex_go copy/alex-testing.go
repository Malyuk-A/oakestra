package main

import (
	"context"
	"fmt"
	"log"
	"syscall"
	"time"

	"github.com/containerd/containerd"
	"github.com/containerd/containerd/cio"
	"github.com/containerd/containerd/namespaces"
	"github.com/containerd/containerd/oci"
)

func main() {
	if err := example(); err != nil {
		log.Fatal(err)
	}
}

func example() error {
	log.Printf("A")
	// create a new client connected to the default socket path for containerd
	client, err := containerd.New("/run/containerd/containerd.sock")
	if err != nil {
		return err
	}
	defer client.Close()

	log.Printf("B")

	// create a new context with an "example" namespace
	ctx := namespaces.WithNamespace(context.Background(), "example")

	// pull the image from DockerHub
	image, err := client.Pull(ctx, "ghcr.io/malyuk-a/fl-client-env-builder:latest", containerd.WithPullUnpack)
	if err != nil {
		return err
	}

	log.Printf("C")

	// create a container
	container, err := client.NewContainer(
		ctx,
		"builder3",
		containerd.WithImage(image),
		containerd.WithNewSnapshot("builder-snapshot3", image),
		containerd.WithNewSpec(oci.WithImageConfig(image)),
	)
	if err != nil {
		return err
	}
	defer container.Delete(ctx, containerd.WithSnapshotCleanup)

	log.Printf("D")

	// create a task from the container
	task, err := container.NewTask(ctx, cio.NewCreator(cio.WithStdio))
	if err != nil {
		return err
	}
	defer task.Delete(ctx)

	log.Printf("E")

	// make sure we wait before calling start
	exitStatusC, err := task.Wait(ctx)
	if err != nil {
		fmt.Println(err)
	}

	log.Printf("F")

	// call start on the task to execute the redis server
	if err := task.Start(ctx); err != nil {
		return err
	}

	log.Printf("G")

	// sleep for a lil bit to see the logs
	time.Sleep(3 * time.Second)

	log.Printf("G2")

	// kill the process and get the exit status
	if err := task.Kill(ctx, syscall.SIGTERM); err != nil {
		return err
	}

	log.Printf("H")

	// wait for the process to fully exit and print out the exit status

	status := <-exitStatusC
	code, _, err := status.Result()
	if err != nil {
		return err
	}
	fmt.Printf("container exited with status: %d\n", code)
	log.Printf("Z")

	return nil
}
