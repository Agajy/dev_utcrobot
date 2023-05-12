#include "waypoint/get_command_list.hpp"

std::string load_file(const std::string& filename){
    std::ifstream file_in;
    file_in.open(filename, std::ifstream::in);

    std::string res;
    std::string temp;


    while(!file_in.eof()) {
        getline(file_in, temp);
        res += temp + "\n";
    }

    return res;

}

std::vector<std::string> extract_command(const std::string& file_content){
    std::vector<std::string> res;
    std::size_t found = file_content.find("command");

    if(found == std::string::npos){
        return res;
    }

    std::size_t start_bracket = file_content.find("[", found+1);
    std::size_t end_bracket = file_content.find("]", found+1);

    if (start_bracket == std::string::npos || end_bracket == std::string::npos){
        return res;
    }

    std::string command_json = file_content.substr(start_bracket+1, end_bracket-start_bracket-1);

    std::size_t start_pos;
    std::size_t end_pose;

    start_pos = command_json.find("\"");
    end_pose = command_json.find("\"", start_pos+1);
    while(start_pos != std::string::npos && end_pose != std::string::npos){
        res.push_back(command_json.substr(start_pos+1, end_pose-start_pos-1));
        start_pos = command_json.find("\"", end_pose+1);
        end_pose = command_json.find("\"", start_pos+1);
    }

    return res;
    
}