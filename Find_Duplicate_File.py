class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        content_to_paths = {} 

        for path in paths:
            path_parts = path.split(' ')  
            directory = path_parts[0]
            files = path_parts[1:]

            for file in files:
                file_info = file.split('(')  
                file_name = file_info[0]
                content = file_info[1][:-1]  

                if content in content_to_paths:
                    content_to_paths[content].append(directory + '/' + file_name)
                else:
                    content_to_paths[content] = [directory + '/' + file_name]

        duplicates = [paths for paths in content_to_paths.values() if len(paths) > 1]

        return duplicates
