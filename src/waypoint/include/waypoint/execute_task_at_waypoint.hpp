#ifndef WAYPOINT__PLUGIN__EXECUTE_TASK_AT_WAYPOINT_HPP_
#define WAYPOINT__PLUGIN__EXECUTE_TASK_AT_WAYPOINT_HPP_

/**
 * While C++17 isn't the project standard. We have to force LLVM/CLang
 * to ignore deprecated declarations
 */
#define _LIBCPP_NO_EXPERIMENTAL_DEPRECATION_WARNING_FILESYSTEM

#include <string>
#include <vector>
#include <stdlib.h>

#include "rclcpp/rclcpp.hpp"
#include "nav2_core/waypoint_task_executor.hpp"


namespace waypoint {

    class ExecuteTaskAtWaypoint: public nav2_core::WaypointTaskExecutor
    {
    public: 
        /**
         * @brief Construct a new Task executor at waypoint object
         *
         */
        ExecuteTaskAtWaypoint() = default;

        /**
         * @brief Destroy a Task Executor At Waypoint object
        */
        ~ExecuteTaskAtWaypoint() override = default;

        /**
         * @brief declares and loads parameters used
         *
         * @param parent parent node that plugin will be created within
         * @param plugin_name should be provided in nav2_params.yaml==> waypoint_follower
         */
        void initialize(
            const rclcpp_lifecycle::LifecycleNode::WeakPtr & parent,
            const std::string & plugin_name) override;

        /**
         * @brief Override this to define the body of your task that you would like to execute once the robot arrived to waypoint
         *
         * @param curr_pose current pose of the robot
         * @param curr_waypoint_index current waypoint, that robot just arrived
         * @return true if task execution was successful
         * @return false if task execution failed
         */
        bool processAtWaypoint(
            const geometry_msgs::msg::PoseStamped & curr_pose, const int & curr_waypoint_index) override;

    protected:
        bool is_enabled_;
        std::string json_path_;
        rclcpp::Logger logger_{rclcpp::get_logger("waypoint")};
        std::vector<std::string> commands_;

    };
}

#endif