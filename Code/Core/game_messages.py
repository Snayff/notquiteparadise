import libtcodpy as libtcod
import textwrap


class Message:
	def __init__(self, text, color=libtcod.white):
		self.text = text
		self.color = color

	def to_json(self):
		json_data = {
			'text': self.text,
			'color': self.color
		}

		return json_data

	@staticmethod
	def from_json(json_data):
		text = json_data.get('text')
		color = json_data.get('color')

		if color:
			message = Message(text, color)
		else:
			message = Message(text)

		return message


class MessageLog:
	def __init__(self, x, width, height):
		self.messages = []
		self.x = x
		self.width = width
		self.height = height

	def add_message(self, message):
		# Split the message if necessary, among multiple lines
		new_msg_lines = textwrap.wrap(message.text, self.width)

		for line in new_msg_lines:
			# If the buffer is full, remove the first line to make room for the new one
			if len(self.messages) == self.height:
				del self.messages[0]

			# Add the new line as a Message object, with the text and the color
			self.messages.append(Message(line, message.color))

	def to_json(self):
			json_data = {
				'x': self.x,
				'width': self.width,
				'height': self.height,
				'messages': [message.to_json() for message in self.messages]
			}

			return json_data

	@staticmethod
	def from_json(json_data):
		x = json_data.get('x')
		width = json_data.get('width')
		height = json_data.get('height')
		messages_json = json_data.get('messages')

		message_log = MessageLog(x, width, height)

		for message_json in messages_json:
			message_log.add_message(Message.from_json(message_json))

		return message_log
