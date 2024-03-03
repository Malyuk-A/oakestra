package main

import (
	"fmt"

	"github.com/containerd/cgroups/v2/cgroup2"
)

func main() {
	fmt.Printf("AAAAAAA")
    //ctx := context.Background()

	//res, _ := cgroup1.Load(cgroups.V1, cgroups.StaticPath("/sys/fs/cgroups/oakestra"))
	res,_ := cgroup2.LoadSystemd("/", "oakestra")

	fmt.Print(res)



    // // Replace "/sys/fs/cgroup/mygroup" with the actual path to your container's cgroup
    // cgroupPath := "/sys/fs/cgroup/oakestra"
    // cg, err := cgroups.Load(cgroups.V2, cgroups.StaticPath(cgroupPath))
    // if err != nil {
    //     fmt.Printf("Failed to load cgroup: %v\n", err)
    //     return
    // }
    // defer cg.Delete(ctx)

    // // Example: Set CPU limit
    // if err := cg.Set(ctx, cgroups.Resource{
    //     CPU: &cgroups.CPU{
    //         Shares: 1024,
    //     },
    // }); err != nil {
    //     fmt.Printf("Failed to set CPU limit: %v\n", err)
    // }
}
