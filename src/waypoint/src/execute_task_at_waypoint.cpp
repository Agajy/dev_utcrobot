#include "waypoint/execute_task_at_waypoint.hpp"
#include "waypoint/get_command_list.hpp"

#include "nav2_util/node_utils.hpp"


namespace waypoint
{

void ExecuteTaskAtWaypoint::initialize(
    const rclcpp_lifecycle::LifecycleNode::WeakPtr & parent,
    const std::string & plugin_name)
{
    auto node = parent.lock();

    nav2_util::declare_parameter_if_not_declared(
        node,
        plugin_name + ".enabled",
        rclcpp::ParameterValue(true)
    );
    nav2_util::declare_parameter_if_not_declared(
        node,
        plugin_name + ".json_path",
        rclcpp::ParameterValue("TOTO")
    );

    node->get_parameter(plugin_name + ".enabled", is_enabled_);
    node->get_parameter(plugin_name + ".json_path", json_path_);

    std::string json_content = load_file(json_path_);    
    commands_ = extract_command(json_content);

    if (!is_enabled_){
        RCLCPP_INFO(
            logger_, "Execute task at waypoint is disabled"
        );
    }
    else{
        RCLCPP_INFO(
            logger_, "Initialize execute task at waypoint;"
        );
    }
}

bool ExecuteTaskAtWaypoint::processAtWaypoint(
    const geometry_msgs::msg::PoseStamped & curr_pose, const int & curr_waypoint_index)
{
    if(!is_enabled_){
        RCLCPP_WARN(
            logger_, "Execute task at waypoint is disabled, not performing anything"
        );
        return true;
    }
    for(int i=0; i<10; i++){
        RCLCPP_INFO(
            logger_, "Waypoint %d : %s", curr_waypoint_index, &commands_[curr_waypoint_index][0]
        );
    }
    system(&commands_[curr_waypoint_index][0]);
    
    return true;
};
}
#include "pluginlib/class_list_macros.hpp"
PLUGINLIB_EXPORT_CLASS(waypoint::ExecuteTaskAtWaypoint, nav2_core::WaypointTaskExecutor)