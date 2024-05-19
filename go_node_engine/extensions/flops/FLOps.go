package flops

import (
	"go_node_engine/logger"
	"os/exec"
	"strings"
)

func HandleFLOpsDataManager() {
	data_manager_sidecar_image := "ghcr.io/malyuk-a/flops-data-manager-sidecar:latest"
	container_name := "flops_data_manager_sidecar"

	cmd := exec.Command("docker", "ps", "-a", "--format", "{{.Names}}")
    output, err := cmd.Output()
    if err!= nil {
        logger.ErrorLogger().Fatalln("Error:", err)
        return
    }

    var containerExists bool
	lines := strings.Split(string(output), "\n")
	for _, line := range lines {
        if line == "" { continue } // Skip empty lines
        if line == container_name {
            containerExists = true
            break
        }
    }

	if !containerExists {
		cmd := exec.Command("docker", "pull", data_manager_sidecar_image)
		err := cmd.Run()
		if err!= nil {
			logger.ErrorLogger().Fatalf("Error pulling FLOps Data Manager image: %v\n", err)
			return
		}
		cmd = exec.Command("docker", "run", "--rm", "-d", "-p", "11027:11027", "-v", "flops_data_manager_sidecar_volume:/flops_data_manager_sidecar_volume" ,"--name=flops_data_manager_sidecar", data_manager_sidecar_image)
		err = cmd.Run()
		if err!= nil {
			logger.ErrorLogger().Fatalf("Error running container: %v\n", err)
			return
		}

    } else {
        logger.InfoLogger().Printf("Container %q already exists.", container_name)
    }

	logger.InfoLogger().Printf("FLOps Data Manager container started successfully.")
}
