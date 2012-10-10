#!/usr/bin/env python


class TimeBlock(object):
	"""
	The TimeBlock object hold several attributes:
	- start time
	- end time
	- What happened during this time

	Created by Olga Botvinnik on 10/09/12 11:31:59
	"""
	def __init__(self, arg):
		super(TimeBlock, self).__init__()
		self.arg = arg
