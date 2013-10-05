# PyAlgoTrade
# 
# Copyright 2013 Gabriel Martin Becedillas Ruiz
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#	http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
.. moduleauthor:: Gabriel Martin Becedillas Ruiz <gabriel.becedillas@gmail.com>
"""

from pyalgotrade import observer

# This will test both the feed and subject interface.
def testBaseFeedInterface(testCase, feed):
	# This tests the observer.Subject interface.
	dispatcher = observer.Dispatcher()
	dispatcher.addSubject(feed)
	dispatcher.run()

	# This tests the feed.BaseFeed interface.
	feed.isRealTime()
	feed.createDataSeries("any", 10)
	feed.getNextValues()


