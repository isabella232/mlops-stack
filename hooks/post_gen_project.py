import os

project_name = "{{cookiecutter.project_name}}"
current_cloud = "{{cookiecutter.cloud}}"
cloud_specific_paths = {
    "azure": [
        os.path.join(".github", "workflows", "scripts", "generate-aad-token.sh"),
        os.path.join(".mlops-setup-scripts", "cicd", "main-azure.tf"),
        os.path.join(".mlops-setup-scripts", "terraform", "main-azure.tf"),
    ],
    "aws": [
        os.path.join(".mlops-setup-scripts", "cicd", "main-aws.tf"),
        os.path.join(".mlops-setup-scripts", "terraform", "main-aws.tf"),
    ],
}

for cloud, paths in cloud_specific_paths.items():
    if cloud != current_cloud:
        for path in paths:
            os.remove(path)


# Remove test files
test_paths = ["_params_testing_only.txt"]
if project_name != "27896cf3-bb3e-476e-8129-96df0406d5c7":
    for path in test_paths:
        os.remove(path)


readme_path = os.path.join(os.getcwd(), "README.md")
print(
    f"Finished generating ML project. See the generated README at {readme_path} for next steps!"
)
