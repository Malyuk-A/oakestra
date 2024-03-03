package virtualization

import (
	"fmt"
	"go_node_engine/logger"
	"go_node_engine/model"
	"os"

	"github.com/containerd/containerd"
)

const LOG_SIZE = 1024

// reads the last 100 bytes of the logfile of a container
func getLogs(serviceID string) string {

	file, err := os.Open(fmt.Sprintf("%s/%s", model.GetNodeInfo().LogDirectory, serviceID))
	if err != nil {
		logger.ErrorLogger().Printf("%v", err)
		return ""
	}
	defer file.Close()

	buf := make([]byte, LOG_SIZE)
	stat, err := file.Stat()
	if err != nil {
		logger.ErrorLogger().Printf("%v", err)
		return ""
	}

	var start int64 = 0
	if stat.Size()-LOG_SIZE < 0 {
		start = 0
	} else {
		start = stat.Size() - LOG_SIZE
	}
	n, err := file.ReadAt(buf, start)
	if err != nil {
		return string(buf[:n])
	}
	return string(buf[:n])
}


func (r *ContainerRuntime) AlexTesting() {

	logger.InfoLogger().Printf("1111111111111111111111111111111")

	test_image := "192.168.178.44:5073/malyuk-a/mlflower-test-a:f63f795f6a7b4094a5a9a0210af45fd121532507"

	var image containerd.Image
	// pull the given image
	sysimg, err := r.contaierClient.ImageService().Get(r.ctx, test_image)
	logger.InfoLogger().Printf("2222222222222222222222222")
	if err == nil {
		logger.InfoLogger().Printf("2aaaaaaaaaaaaaaaaaaa")
		image = containerd.NewImage(r.contaierClient, sysimg)
	} else {
		logger.InfoLogger().Printf("2bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb")
		logger.InfoLogger().Printf("Error retrieving the image: %v \n Trying to pull the image online.", err)

		logger.ErrorLogger().Printf("Error retrieving the image: %v \n Trying to pull the image online.", err)

		logger.InfoLogger().Printf("2b1111111111111111111111")
		image, err = r.contaierClient.Pull(r.ctx, test_image, containerd.WithPullUnpack)
		logger.InfoLogger().Printf("2b22222222222222222222222")
		if err != nil {
			logger.InfoLogger().Printf("2bAAAAAAAAAAAAAA")
			return
		}
		logger.InfoLogger().Printf("2bBBBBBBBBBBBBBBBBBBBBBB")
	}
	logger.InfoLogger().Printf("3333333333333333333333333333")
	logger.InfoLogger().Printf(image.Name())
}	
