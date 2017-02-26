from twilio.rest import TwilioRestClient

class text_alerts(object):
    def textMe():
        client = TwilioRestClient()

        client.messages.create(from_="9546842274",
                               to="9546274969",
                               body="Check your child immediately"
