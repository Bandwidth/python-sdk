"""
test_bxml.py

Unit tests for BXML

@copyright Bandwidth Inc.
"""
from bandwidth.voice.bxml.response import Response
from bandwidth.voice.bxml.bxml import Bxml
from bandwidth.voice.bxml.verbs import *
from bandwidth.webrtc.utils import *


class TestBxml:
    """
    Class for the BXML tests
    """

    def test_forward_xml_with_optional_fields(self):
        response = Response()
        forward = Forward(
            to="+10987654321",
            from_="+11234567890",
            call_timeout=100,
            diversion_treatment="propagate",
            diversion_reason="away"
        )
        response.add_verb(forward)
        expected_bxml = '<?xml version="1.0" encoding="UTF-8"?><Response><Forward to="+10987654321" callTimeout="100" from="+11234567890" diversionTreatment="propagate" diversionReason="away"/></Response>'
        assert response.to_bxml() == expected_bxml

    def test_gather_no_nested(self):
        response = Response()
        gather = Gather(
            gather_url="https://gather.url/nextBXML",
            gather_method="POST",
            terminating_digits="#",
            tag="tag",
            max_digits=20,
            inter_digit_timeout=50,
            username="user",
            password="password",
            first_digit_timeout=10,
            repeat_count=3,
            gather_fallback_url="https://test.com",
            gather_fallback_method="GET",
            fallback_username="fuser",
            fallback_password="fpass"
        )
        response.add_verb(gather)
        expected_bxml = '<?xml version="1.0" encoding="UTF-8"?><Response><Gather gatherUrl="https://gather.url/nextBXML" gatherMethod="POST" terminatingDigits="#" tag="tag" maxDigits="20" interDigitTimeout="50" username="user" password="password" firstDigitTimeout="10" repeatCount="3" gatherFallbackUrl="https://test.com" gatherFallbackMethod="GET" fallbackUsername="fuser" fallbackPassword="fpass"/></Response>'
        assert response.to_bxml() == expected_bxml

    def test_gather_with_speak_sentence(self):
        response = Response()
        speak_sentence = SpeakSentence(
            sentence="Phrase.",
            voice="kate",
            locale="en_US",
            gender="female"
        )
        gather = Gather(
            gather_url="https://gather.url/nextBXML",
            gather_method="POST",
            terminating_digits="#",
            tag="tag",
            max_digits=20,
            inter_digit_timeout=50,
            username="user",
            password="password",
            first_digit_timeout=10,
            repeat_count=3,
            speak_sentence=speak_sentence
        )
        expected_bxml = '<?xml version="1.0" encoding="UTF-8"?><Response><Gather gatherUrl="https://gather.url/nextBXML" gatherMethod="POST" terminatingDigits="#" tag="tag" maxDigits="20" interDigitTimeout="50" username="user" password="password" firstDigitTimeout="10" repeatCount="3"><SpeakSentence voice="kate" locale="en_US" gender="female">Phrase.</SpeakSentence></Gather></Response>'
        response.add_verb(gather)
        assert response.to_bxml() == expected_bxml

    def test_gather_play_audio(self):
        response = Response()
        play_audio_1 = PlayAudio(url="https://audio.url/audio1.wav")
        gather = Gather(
            gather_url="https://gather.url/nextBXML",
            gather_method="POST",
            terminating_digits="#",
            tag="tag",
            max_digits=20,
            inter_digit_timeout=50,
            username="user",
            password="password",
            first_digit_timeout=10,
            repeat_count=3,
            play_audio=play_audio_1
        )
        expected_bxml = '<?xml version="1.0" encoding="UTF-8"?><Response><Gather gatherUrl="https://gather.url/nextBXML" gatherMethod="POST" terminatingDigits="#" tag="tag" maxDigits="20" interDigitTimeout="50" username="user" password="password" firstDigitTimeout="10" repeatCount="3"><PlayAudio>https://audio.url/audio1.wav</PlayAudio></Gather></Response>'
        response.add_verb(gather)
        assert response.to_bxml() == expected_bxml

    def test_hangup(self):
        response = Response()
        hang_up = Hangup()
        response.add_verb(hang_up)
        expected_bxml = '<?xml version="1.0" encoding="UTF-8"?><Response><Hangup/></Response>'
        assert response.to_bxml() == expected_bxml

    def test_pause(self):
        response = Response()
        pause = Pause(duration=400)
        response.add_verb(pause)
        expected_bxml = '<?xml version="1.0" encoding="UTF-8"?><Response><Pause duration="400"/></Response>'
        assert response.to_bxml() == expected_bxml

    def test_pause_recording(self):
        response = Response()
        pause_recording = PauseRecording()
        response.add_verb(pause_recording)
        expected_bxml = '<?xml version="1.0" encoding="UTF-8"?><Response><PauseRecording/></Response>'
        assert response.to_bxml() == expected_bxml

    def test_play_audio(self):
        response = Response()
        play_audio_1 = PlayAudio(
            url="https://audio.url/audio1.wav",
            username="user",
            password="pass"
        )
        response.add_verb(play_audio_1)
        expected_bxml = '<?xml version="1.0" encoding="UTF-8"?><Response><PlayAudio username="user" password="pass">https://audio.url/audio1.wav</PlayAudio></Response>'
        assert response.to_bxml() == expected_bxml

    def test_record(self):
        response = Response()
        record = Record(
            tag="tag",
            username="user",
            password="pass",
            record_complete_url="https://record.url.server/record",
            record_complete_method="POST",
            recording_available_url="https://record.url.server/available",
            recording_available_method="GET",
            terminating_digits="#",
            max_duration=90,
            file_format="mp3",
            transcribe=False,
            transcription_available_url="https://transcribe.url.server/available",
            transcription_available_method="POST",
            silence_timeout=90,
            record_complete_fallback_url="https://test.com",
            record_complete_fallback_method="GET",
            fallback_username="fuser",
            fallback_password="fpass"
        )
        response.add_verb(record)
        expected_bxml = '<?xml version="1.0" encoding="UTF-8"?><Response><Record tag="tag" username="user" password="pass" recordCompleteUrl="https://record.url.server/record" recordCompleteMethod="POST" recordingAvailableUrl="https://record.url.server/available" recordingAvailableMethod="GET" terminatingDigits="#" maxDuration="90" fileFormat="mp3" transcribe="false" transcriptionAvailableUrl="https://transcribe.url.server/available" transcriptionAvailableMethod="POST" silenceTimeout="90" recordCompleteFallbackUrl="https://test.com" recordCompleteFallbackMethod="GET" fallbackUsername="fuser" fallbackPassword="fpass"/></Response>'
        assert response.to_bxml() == expected_bxml

    def test_redirect(self):
        response = Response()
        redirect = Redirect(
            redirect_url="http://flow.url/newFlow",
            redirect_method="POST",
            tag="tag",
            username="user",
            password="pass",
            redirect_fallback_url="https://test.com",
            redirect_fallback_method="GET",
            fallback_username="fuser",
            fallback_password="fpass"
        )
        response.add_verb(redirect)
        expected_bxml = '<?xml version="1.0" encoding="UTF-8"?><Response><Redirect redirectUrl="http://flow.url/newFlow" redirectMethod="POST" tag="tag" username="user" password="pass" redirectFallbackUrl="https://test.com" redirectFallbackMethod="GET" fallbackUsername="fuser" fallbackPassword="fpass"/></Response>'
        assert response.to_bxml() == expected_bxml

    def test_resume_recording(self):
        response = Response()
        resume_recording = ResumeRecording()
        response.add_verb(resume_recording)
        expected_bxml = '<?xml version="1.0" encoding="UTF-8"?><Response><ResumeRecording/></Response>'
        assert (response.to_bxml() == expected_bxml)

    def test_dtmf(self):
        response = Response()
        send_dtmf = SendDtmf(
            dtmf="1234",
            tone_duration=200,
            tone_interval=450
        )
        expected_bxml = '<?xml version="1.0" encoding="UTF-8"?><Response><SendDtmf toneDuration="200" toneInterval="450">1234</SendDtmf></Response>'
        response.add_verb(send_dtmf)
        assert response.to_bxml() == expected_bxml

    def test_speak_sentence(self):
        response = Response()
        speak_sentence = SpeakSentence(
            sentence="Phrase.",
            voice="kate",
            locale="en_US",
            gender="female"
        )
        expected_bxml = '<?xml version="1.0" encoding="UTF-8"?><Response><SpeakSentence voice="kate" locale="en_US" gender="female">Phrase.</SpeakSentence></Response>'
        response.add_verb(speak_sentence)
        assert response.to_bxml() == expected_bxml

    def test_speak_sentence_SSML(self):
        response = Response()
        speak_sentence = SpeakSentence(
            sentence='<lang xml:lang="es-MX">Hydrogen</lang> is the most abundant element in the universe.',
            voice="kate",
            locale="en_US",
            gender="female"
        )
        expected_bxml = '<?xml version="1.0" encoding="UTF-8"?><Response><SpeakSentence voice="kate" locale="en_US" gender="female"><lang xml:lang="es-MX">Hydrogen</lang> is the most abundant element in the universe.</SpeakSentence></Response>'
        response.add_verb(speak_sentence)
        assert response.to_bxml() == expected_bxml

    def test_start_recording(self):
        response = Response()
        record = StartRecording(
            tag="tag",
            username="user",
            password="pass",
            recording_available_url="https://record.url.server/available",
            recording_available_method="GET",
            file_format="mp3",
            multi_channel=True,
            transcribe=False,
            transcription_available_url="https://transcribe.url.server/available",
            transcription_available_method="POST"
        )
        response.add_verb(record)
        expected_bxml = '<?xml version="1.0" encoding="UTF-8"?><Response><StartRecording tag="tag" username="user" password="pass" recordingAvailableUrl="https://record.url.server/available" recordingAvailableMethod="GET" fileFormat="mp3" multiChannel="true" transcribe="false" transcriptionAvailableUrl="https://transcribe.url.server/available" transcriptionAvailableMethod="POST"/></Response>'
        assert response.to_bxml() == expected_bxml

    def test_stop_recording(self):
        response = Response()
        stop_recording = StopRecording()
        response.add_verb(stop_recording)
        expected_bxml = '<?xml version="1.0" encoding="UTF-8"?><Response><StopRecording/></Response>'
        assert response.to_bxml() == expected_bxml

    def test_transfer(self):
        response = Response()
        phone1 = PhoneNumber(
            number="+11234567891",
            transfer_answer_url="https://transfer.com/answer",
            transfer_answer_method="POST",
            username="user",
            password="pass",
            tag="tag",
            transfer_disconnect_method="POST",
            transfer_disconnect_url="https://transfer.com/disconnect",
            transfer_answer_fallback_url="https://test.com",
            transfer_answer_fallback_method="GET",
            fallback_username="fuser",
            fallback_password="fpass"
        )
        phone1_bxml = '<PhoneNumber transferAnswerUrl="https://transfer.com/answer" transferAnswerMethod="POST" username="user" password="pass" tag="tag" transferDisconnectMethod="POST" transferDisconnectUrl="https://transfer.com/disconnect" transferAnswerFallbackUrl="https://test.com" transferAnswerFallbackMethod="GET" fallbackUsername="fuser" fallbackPassword="fpass">+11234567891</PhoneNumber>'
        phone2 = PhoneNumber(number="+11234567892")
        phone2_bxml = '<PhoneNumber>+11234567892</PhoneNumber>'
        transfer = Transfer(
            transfer_caller_id="+15555555555",
            call_timeout=50,
            tag="tag",
            transfer_complete_url="https://transcribe.url.server/complete",
            transfer_complete_method="POST",
            username="user",
            password="pass",
            diversion_treatment="propagate",
            diversion_reason="away",
            phone_numbers=[phone1, phone2],
            transfer_complete_fallback_url="https://test.com",
            transfer_complete_fallback_method="GET",
            fallback_username="fusern",
            fallback_password="fpassw"
        )
        response.add_verb(transfer)
        expected_bxml = f'<?xml version="1.0" encoding="UTF-8"?><Response><Transfer transferCallerId="+15555555555" callTimeout="50" tag="tag" transferCompleteUrl="https://transcribe.url.server/complete" transferCompleteMethod="POST" username="user" password="pass" diversionTreatment="propagate" diversionReason="away" transferCompleteFallbackUrl="https://test.com" transferCompleteFallbackMethod="GET" fallbackUsername="fusern" fallbackPassword="fpassw">{phone1_bxml}{phone2_bxml}</Transfer></Response>'

        print(response.to_bxml())
        print(expected_bxml)

        assert response.to_bxml() == expected_bxml

    def test_conference(self):
        conference = Conference(
            "my-conference",
            mute=False,
            hold=True,
            call_ids_to_coach="c-123,c-345",
            conference_event_url="https://test.com",
            conference_event_method="GET",
            username="user",
            password="pass",
            tag="tag",
            conference_event_fallback_url="https://test2.com",
            conference_event_fallback_method="POST",
            fallback_username="fuser",
            fallback_password="fpass"
        )

        response = Response()
        response.add_verb(conference)
        expected_bxml = '<?xml version="1.0" encoding="UTF-8"?><Response><Conference mute="false" hold="true" callIdsToCoach="c-123,c-345" conferenceEventUrl="https://test.com" conferenceEventMethod="GET" tag="tag" username="user" password="pass" conferenceEventFallbackUrl="https://test2.com" conferenceEventFallbackMethod="POST" fallbackUsername="fuser" fallbackPassword="fpass">my-conference</Conference></Response>'
        assert response.to_bxml() == expected_bxml

    def test_conference_coach_array(self):
        conference = Conference(
            "my-conference", call_ids_to_coach=["c-123", "c-456"])
        response = Response()
        response.add_verb(conference)
        expected_bxml = '<?xml version="1.0" encoding="UTF-8"?><Response><Conference callIdsToCoach="c-123,c-456">my-conference</Conference></Response>'
        assert response.to_bxml() == expected_bxml

    def test_bridge(self):
        bridge = Bridge("c-95ac8d6e-1a31c52e-b38f-4198-93c1-51633ec68f8d",
                        bridge_complete_url="https://test.com",
                        bridge_complete_method="GET",
                        bridge_target_complete_url="https://test2.com",
                        bridge_target_complete_method="POST",
                        username="user",
                        password="pass",
                        tag="custom tag",
                        bridge_complete_fallback_url="https://test3.com",
                        bridge_complete_fallback_method="GET",
                        bridge_target_complete_fallback_url="https://test4.com",
                        bridge_target_complete_fallback_method="POST",
                        fallback_username="fuser",
                        fallback_password="fpass"
                        )

        response = Response()
        response.add_verb(bridge)
        expected_bxml = '<?xml version="1.0" encoding="UTF-8"?><Response><Bridge bridgeCompleteUrl="https://test.com" bridgeCompleteMethod="GET" bridgeTargetCompleteUrl="https://test2.com" bridgeTargetCompleteMethod="POST" username="user" password="pass" tag="custom tag" bridgeCompleteFallbackUrl="https://test3.com" bridgeCompleteFallbackMethod="GET" bridgeTargetCompleteFallbackUrl="https://test4.com" bridgeTargetCompleteFallbackMethod="POST" fallbackUsername="fuser" fallbackPassword="fpass">c-95ac8d6e-1a31c52e-b38f-4198-93c1-51633ec68f8d</Bridge></Response>'
        assert response.to_bxml() == expected_bxml

    def test_ring(self):
        ring = Ring(
            duration=5,
            answer_call=False
        )

        response = Response()
        response.add_verb(ring)
        expected_bxml = '<?xml version="1.0" encoding="UTF-8"?><Response><Ring duration="5" answerCall="False"/></Response>'
        assert (response.to_bxml() == expected_bxml)

    def test_start_gather(self):
        startGather = StartGather(
            dtmfUrl="https://test.com",
            dtmfMethod="POST",
            username="user",
            password="pass",
            tag="custom tag"
        )

        response = Response()
        response.add_verb(startGather)
        expected_bxml = '<?xml version="1.0" encoding="UTF-8"?><Response><StartGather dtmfUrl="https://test.com" dtmfMethod="POST" username="user" password="pass" tag="custom tag"/></Response>'
        assert response.to_bxml() == expected_bxml

    def test_stop_gather(self):
        stopGather = StopGather()

        response = Response()
        response.add_verb(stopGather)
        expected_bxml = '<?xml version="1.0" encoding="UTF-8"?><Response><StopGather/></Response>'
        assert response.to_bxml() == expected_bxml

    def test_gather_speak_sentence_ssml(self):
        response = Response()
        speak_sentence = SpeakSentence(
            sentence='Hello. Your number is <say-as interpret-as="telephone">asdf</say-as>, lets play a game. What is 10 + 3. Press the pound key when finished.'
        )
        gather = Gather(
            speak_sentence=speak_sentence
        )
        expected_bxml = '<?xml version="1.0" encoding="UTF-8"?><Response><Gather><SpeakSentence>Hello. Your number is <say-as interpret-as="telephone">asdf</say-as>, lets play a game. What is 10 + 3. Press the pound key when finished.</SpeakSentence></Gather></Response>'
        response.add_verb(gather)
        assert response.to_bxml() == expected_bxml

    def test_empty_bxml_verb(self):
        expected_bxml = '<?xml version="1.0" encoding="UTF-8"?><Bxml></Bxml>'

        bxml = Bxml()
        assert bxml.to_bxml() == expected_bxml

    def test_bxml_speak_sentence_pause(self):
        expected_bxml = '<?xml version="1.0" encoding="UTF-8"?><Bxml><SpeakSentence voice="Julie">Wee Woo</SpeakSentence><Pause duration="10"/></Bxml>'
        bxml = Bxml()
        speak_sentence = SpeakSentence(
            voice="Julie",
            sentence="Wee Woo"
        )
        pause = Pause(10)
        bxml.add_verb(speak_sentence)
        bxml.add_verb(pause)
        assert bxml.to_bxml() == expected_bxml

    def test_generate_transfer_bxml(self):
        expected = '<?xml version="1.0" encoding="UTF-8"?><Response><Transfer><SipUri uui="93d6f3c0be5845960b744fa28015d8ede84bd1a4;encoding=base64,asdf;encoding=jwt">sip:sipx.webrtc.bandwidth.com:5060</SipUri></Transfer></Response>'
        actual = generate_transfer_bxml(
            'asdf', 'c-93d6f3c0-be584596-0b74-4fa2-8015-d8ede84bd1a4')
        assert actual == expected

    def test_generate_transfer_bxml_verb(self):
        expected = '<Transfer><SipUri uui="93d6f3c0be5845960b744fa28015d8ede84bd1a4;encoding=base64,asdf;encoding=jwt">sip:sipx.webrtc.bandwidth.com:5060</SipUri></Transfer>'
        actual = generate_transfer_bxml_verb(
            'asdf', 'c-93d6f3c0-be584596-0b74-4fa2-8015-d8ede84bd1a4')
        assert actual == expected
    
    
