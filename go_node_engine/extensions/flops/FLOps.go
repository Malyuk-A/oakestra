package flops

import (
	"go_node_engine/logger"
	"os/exec"
	"strings"
)

func HandleFLOpsDataManager() {
	data_manager_image := "ghcr.io/malyuk-a/flops-data-manager:latest"
	container_name := "flops_data_manager"

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
		cmd := exec.Command("docker", "pull", data_manager_image)
		err := cmd.Run()
		if err!= nil {
			logger.ErrorLogger().Fatalf("Error pulling FLOps Data Manager image: %v\n", err)
			return
		}
		cmd = exec.Command("docker", "run", "--rm", "-d", "-p", "11027:11027", "-v", "flops_data_manager_sidecar_volume:/flops_data_manager_sidecar_volume" ,"--name=flops_data_manager", data_manager_image)
		err = cmd.Run()
		if err!= nil {
			logger.ErrorLogger().Fatalf("Error running container: %v\n", err)
			return
		}

    } else {
        logger.InfoLogger().Printf("Container %q already exists.", container_name)
    }

	

	// version: "3.3"

	// services:
	
	//   ml_data_manager:
	// 	image: ml_data_manager
	// 	build: .
	// 	hostname: ml_data_manager
	// 	container_name: ml_data_manager
	// 	expose:
	// 	  - "11027"
	// 	ports:
	// 	  - "11027:11027"
	// 	volumes:
	// 	  - ml_data_volume:/ml_data_volume
		  
	// volumes:
	//   ml_data_volume:
	

	

	logger.InfoLogger().Printf("FLOps Data Manager container started successfully.")
}
