import glob
import boto3
import os
from time import sleep
from platform import system as os_name


def main():
    try:
        count = 0
        polly_client = boto3.Session(aws_access_key_id='your_key_id',
                                     aws_secret_access_key='you_secret_key',
                                     region_name='us-west-2').client('polly')

        # files should be in the same folder
        files = sorted(glob.glob(f'{os.getcwd()}/*.txt'), key=len)
        for n, file_name in enumerate(files):
            print(f'{n+1} | {file_name}')
            count += 1
            with open(file_name, 'r') as file_handle:
                text = file_handle.read()
                response = polly_client.synthesize_speech(VoiceId='Joanna',
                                                          OutputFormat='mp3',
                                                          Text=text)
                file = open(f'{count} speech.mp3', 'wb')
                file.write(response['AudioStream'].read())
                file.close()

    except OSError as error:
        print('An exception has occurred', error)


if __name__ == "__main__":
    main()
