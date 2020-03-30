from google.cloud import speech_v1
from google.cloud.speech_v1 import enums

def sample_long_running_recognize(storage_uri):
    client = speech_v1.SpeechClient()

    sample_rate_hertz = 48000

    language_code = "en-US"

    encoding = enums.RecognitionConfig.AudioEncoding.ENCODING_UNSPECIFIED
    config = {
        "sample_rate_hertz": sample_rate_hertz,
        "language_code": language_code,
        "encoding": encoding,
    }
    audio = {"uri": storage_uri}

    operation = client.long_running_recognize(config, audio)

    print(u"Waiting for operation to complete...")
    response = operation.result()

    for result in response.results:
        alternative = result.alternatives[0]
        print(u"Transcript: {}".format(alternative.transcript))

sample_long_running_recognize("gs://ev-transcript/trans.mp3")
