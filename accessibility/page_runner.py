import subprocess
from accessibility.features.environment import FILE_NAME
from environment_variables import PAGES_LIST, BASE_URL, QA_FOLDER_PATH

# Adding home to the page list as it works here.
all_pages = PAGES_LIST
all_pages.append('/')

for page in all_pages:
    generated_command = ''
    if page == '/':
        generated_command = 'docker run \
            -v $PWD/%saccessibility/output/:/lighthouse/output/  \
            -i matthiaswinkelmann/lighthouse-chromium-alpine \
            --output json --output html \
            --output-path=/lighthouse/output/%s %s%s' % (
            QA_FOLDER_PATH,
            FILE_NAME,
            BASE_URL,
            page
        )

    process = subprocess.Popen(
        generated_command,
        stderr=subprocess.STDOUT,
        shell=True
    )
    process.wait()


for page in all_pages:
    generated_command = ''
    if page == '/':
        generated_command = 'FILE_NAME=%s behave %saccessibility/features' % (
            'index',
            QA_FOLDER_PATH
        )
    else:
        generated_command = 'FILE_NAME=%s behave %saccessibility/features' % (
            page.replace('/', ''),
            QA_FOLDER_PATH
        )
    process = subprocess.Popen(
        generated_command,
        stderr=subprocess.STDOUT,
        shell=True
    )
    process.wait()