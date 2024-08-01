# Example of absolute paths
absolute_linux_path = "/usr/local/bin/some_executable"
absolute_windows_path = "C:\\Program Files\\SomeApp\\app.exe"

# Relative paths (should not trigger the hook)
relative_path1 = "./relative/path/to/file.txt"
relative_path2 = "../another/relative/path/to/file.txt"

# Mixed paths
mixed_path1 = "/absolute/path/with/relative/./elements"
mixed_path2 = "C:\\absolute\\path\\with\\relative\\elements\\."

abs_path_linux = "/this/is/a/commented/absolute/path"
abs_path_windows = "C:\\this\\is\\a\\commented\\absolute\\path"
