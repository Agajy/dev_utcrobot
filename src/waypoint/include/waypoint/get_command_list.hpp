#ifndef WAYPOINT__GET_COMMAND_LIST_
#define WAYPOINT__GET_COMMAND_LIST_

#include <string>
#include <vector>
#include <fstream>

std::string load_file(const std::string&);
std::vector<std::string> extract_command(const std::string&);

#endif