import requests

class CallPoll:

	def __init__(self, server, url = "https://mantled-timer.000webhostapp.com/ppp.php", wait = 25):

		self.url = url
		self.server = server
		self.session = requests.session()
		self.wait = wait
		self.routes = []

	def check(self):
		try:
			response = self.session.get(
				f"{self.url}/poll/{self.server}",
				timeout=self.wait + 10
			)
		except:
			return []

		if not response.text:
			return []
		
		for event in response.json():
			yield event

	def send_response(self, ev_id, response):
		r = self.session.post(
			f"{self.url}/answer/{self.server}",
			data = {
				"event_id": ev_id,
				"answer": response}
		)

	def route(self, func):
		self.routes.append(func)
		def decorator():
			self.routes.append(func)
		return decorator

	def run(self):
		while True:
			for event in self.check():
				ev_id = event["event_id"]
				self.send_response(ev_id = ev_id, response = self.routes[0](event["data"]))

