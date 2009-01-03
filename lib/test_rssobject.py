import rssobject
import test_htmldiff


def assertXMLEqual(source, pattern):
    result = test_htmldiff.htmlcompareError(source, pattern)
    if result:
        assert 0, result

params_testCreates = []

def do_testCreates(name, kw, itemKW, output):
    items = [rssobject.RSSItem(**kw) for kw in itemKW]
    rss = rssobject.RSS(metadata=kw, items=items)
    assertXMLEqual(str(rss), output)

params_testRoundTrip = []

def test_creates():
    for params in params_testCreates:
        do_testCreates(*params)

def do_testRoundTrip(name, input):
    rss = rssobject.RSS(text=input)
    assertXMLEqual(str(rss), input)

def test_roundtrip():
    for params in params_testRoundTrip:
        do_testRoundTrip(*params)

def addCreate(name, output, **kw):
    itemKW = kw['items']
    del kw['items']
    params_testCreates.append((name, kw, itemKW, output))

def addRoundTrip(name, input):
    params_testRoundTrip.append((name, input))

addCreate(
    'simple',
    '''<?xml version="1.0">
    <rss version="2.0">
    <channel>
    <lastBuildDate>now</lastBuildDate>
    <generator>*</generator>
    <pubDate>now</pubDate>
    </channel>
    </rss>''',
    lastBuildDate='now',
    pubDate='now',
    items=[])

addCreate(
    'complex',
    '''<?xml version="1.0">
    <rss version="2.0">
    <channel>
    <lastBuildDate>*</lastBuildDate>
    <pubDate>Tuesday</pubDate>
    <generator>rssobject.py v0.1</generator>
    <author>ianb@colorstudy.com</author>
    <title>second</title>
    <guid>http://testblog.com/item2.html</guid>
    <item>
      <guid>http://testblog.com/item1.html</guid>
      <link>http://testblog.com/item1.html</link>
      <description>My first post!</description>
      <pubDate>*</pubDate>
      <title>First post!</title>
    </item>
    <item>
      <guid>http://testblog.com/item2.html</guid>
      <link>http://testblog.com/item2.html</link>
      <author>ianb@colorstudy.com</author>
      <pubDate>Tuesday</pubDate>
      <title>second</title>
    </item>
    </channel>
    </rss>
    ''',
    title='test',
    link='http://testblog.com',
    description='A cool test blog',
    ttl=20,
    author='ianb@colorstudy.com',
    items=[{'title': 'First post!',
            'link': 'http://testblog.com/item1.html',
            'description': 'My first post!'},
           {'title': 'second',
            'guid': 'http://testblog.com/item2.html',
            'pubDate': 'Tuesday',
            'author': 'ianb@colorstudy.com'}],
    )

addRoundTrip(
    'rssExample',
    """<?xml version="1.0"?>
<rss version="2.0">
	<channel>
		<title>Scripting News</title>
		<link>http://www.scripting.com/</link>
		<description>A weblog about scripting and stuff like that.</description>
		<language>en-us</language>

		<copyright>Copyright 1997-2002 Dave Winer</copyright>
		<lastBuildDate>Mon, 30 Sep 2002 11:00:00 GMT</lastBuildDate>
		<docs>http://backend.userland.com/rss</docs>

		<generator>Radio UserLand v8.0.5</generator>
		<managingEditor>dave@userland.com</managingEditor>
		<webMaster>dave@userland.com</webMaster>
		<ttl>40</ttl>
			<pubDate>Fri 09 Apr 2004 12:00:00 GMT</pubDate>
		<item>

			<description>&quot;rssflowersalignright&quot;With any luck we should have one or two more days of namespaces stuff here on Scripting News. It feels like it's winding down. Later in the week I'm going to a &lt;a href=&quot;http://harvardbusinessonline.hbsp.harvard.edu/b02/en/conferences/conf_detail.jhtml?id=s775stg&amp;pid=144XCF&quot;&gt;conference&lt;/a&gt; put on by the Harvard Business School. So that should change the topic a bit. The following week I'm off to Colorado for the &lt;a href=&quot;http://www.digitalidworld.com/conference/2002/index.php&quot;&gt;Digital ID World&lt;/a&gt; conference. We had to go through namespaces, and it turns out that weblogs are a great way to work around mail lists that are clogged with &lt;a href=&quot;http://www.userland.com/whatIsStopEnergy&quot;&gt;stop energy&lt;/a&gt;. I think we solved the problem, have reached a consensus, and will be ready to move forward shortly.</description>

			<pubDate>Mon, 30 Sep 2002 01:56:02 GMT</pubDate>
			<guid>http://scriptingnews.userland.com/backissues/2002/09/29#When:6:56:02PM</guid>
				<link>http://scriptingnews.userland.com/backissues/2002/09/29#When:6:56:02PM</link>
			</item>
		<item>
			<description>Joshua Allen: &lt;a href=&quot;http://www.netcrucible.com/blog/2002/09/29.html#a243&quot;&gt;Who loves namespaces?&lt;/a&gt;</description>

			<pubDate>Sun, 29 Sep 2002 19:59:01 GMT</pubDate>
			<guid>http://scriptingnews.userland.com/backissues/2002/09/29#When:12:59:01PM</guid>
			<link>http://scriptingnews.userland.com/backissues/2002/09/29#When:12:59:01PM</link>
			</item>
		<item>
			<description>&lt;a href=&quot;http://www.docuverse.com/blog/donpark/2002/09/29.html#a68&quot;&gt;Don Park&lt;/a&gt;: &quot;It is too easy for engineer to anticipate too much and XML Namespace is a frequent host of over-anticipation.&quot;</description>

			<pubDate>Mon, 30 Sep 2002 01:52:02 GMT</pubDate>
			<guid>http://scriptingnews.userland.com/backissues/2002/09/29#When:6:52:02PM</guid>
			<link>http://scriptingnews.userland.com/backissues/2002/09/29#When:6:52:02PM</link>
			</item>
		<item>
			<description>&lt;a href=&quot;http://scriptingnews.userland.com/stories/storyReader$1768&quot;&gt;Three Sunday Morning Options&lt;/a&gt;. &quot;I just got off the phone with Tim Bray, who graciously returned my call on a Sunday morning while he was making breakfast for his kids.&quot; We talked about three options for namespaces in RSS 2.0, and I think I now have the tradeoffs well outlined, and ready for other developers to review. If there is now a consensus, I think we can easily move forward. </description>

			<pubDate>Sun, 29 Sep 2002 17:05:20 GMT</pubDate>
			<guid>http://scriptingnews.userland.com/backissues/2002/09/29#When:10:05:20AM</guid>
			<link>http://scriptingnews.userland.com/backissues/2002/09/29#When:10:05:20AM</link>
			</item>
		<item>
			<description>&lt;a href=&quot;http://blog.mediacooperative.com/mt-comments.cgi?entry_id=1435&quot;&gt;Mark Pilgrim&lt;/a&gt; weighs in behind option 1 on a Ben Hammersley thread. On the RSS2-Support list, Phil Ringnalda lists a set of &lt;a href=&quot;http://groups.yahoo.com/group/RSS2-Support/message/54&quot;&gt;proposals&lt;/a&gt;, the first is equivalent to option 1. </description>

			<pubDate>Sun, 29 Sep 2002 19:09:28 GMT</pubDate>
			<guid>http://scriptingnews.userland.com/backissues/2002/09/29#When:12:09:28PM</guid>
			<link>http://scriptingnews.userland.com/backissues/2002/09/29#When:12:09:28PM</link>
			</item>
		<item>
			<description>&lt;a href=&quot;http://effbot.org/zone/effnews-4.htm&quot;&gt;Fredrik Lundh breaks&lt;/a&gt; through, following Simon Fell's lead, now his Python aggregator works with Scripting News &lt;a href=&quot;http://www.scripting.com/rss.xml&quot;&gt;in&lt;/a&gt; RSS 2.0. BTW, the spec is imperfect in regards to namespaces. We anticipated a 2.0.1 and 2.0.2 in the Roadmap for exactly this purpose. Thanks for your help, as usual, Fredrik. </description>

			<pubDate>Sun, 29 Sep 2002 15:01:02 GMT</pubDate>
			<guid>http://scriptingnews.userland.com/backissues/2002/09/29#When:8:01:02AM</guid>
			<link>http://scriptingnews.userland.com/backissues/2002/09/29#When:8:01:02AM</link>
			</item>
		<item>
			<title>Law and Order</title>
			<link>http://scriptingnews.userland.com/backissues/2002/09/29#lawAndOrder</link>
			<description>

				&lt;p&gt;&lt;a href=&quot;http://www.nbc.com/Law_&amp;_Order/index.html&quot;&gt;&lt;img src=&quot;http://radio.weblogs.com/0001015/images/2002/09/29/lenny.gif&quot; width=&quot;45&quot; height=&quot;53&quot; border=&quot;0&quot; align=&quot;right&quot; hspace=&quot;15&quot; vspace=&quot;5&quot; alt=&quot;A picture named lenny.gif&quot;&gt;&lt;/a&gt;A great line in a recent Law and Order. Lenny Briscoe, played by Jerry Orbach, is interrogating a suspect. The suspect tells a story and reaches a point where no one believes him, not even the suspect himself. Lenny says: &quot;Now there's five minutes of my life that's lost forever.&quot; &lt;/p&gt;

				</description>
			<pubDate>Sun, 29 Sep 2002 23:48:33 GMT</pubDate>
			<guid>http://scriptingnews.userland.com/backissues/2002/09/29#lawAndOrder</guid>
			</item>
		<item>
			<title>Rule 1</title>
			<link>http://scriptingnews.userland.com/backissues/2002/09/29#rule1</link>

			<description>
				&lt;p&gt;In the discussions over namespaces in RSS 2.0, one thing I hear a lot of, that is just plain wrong, is that when you move up by a major version number, breakage is expected and is okay. In the world I come from it is, emphatically, &lt;i&gt;not okay.&lt;/i&gt; We spend huge resources to make sure that files, scripts and apps built in version N work in version N+1 without modification. Even the smallest change in the core engine can break apps. It's just not acceptable. When we make changes we have to be sure there's no breakage. I don't know where these other people come from, or if they make software that anyone uses, but the users I know don't stand for that. As we expose the tradeoffs it becomes clear that &lt;i&gt;that's the issue here.&lt;/i&gt; We are not in Year Zero. There are users. Breaking them is not an option. A conclusion to lift the confusion: Version 0.91 and 0.92 files are valid 2.0 files. This is where we started, what seems like years ago.&lt;/p&gt;

				&lt;p&gt;BTW, you can ask anyone who's worked for me in a technical job to explain rules 1 and 1b. (I'll clue you in. Rule 1 is &quot;No Breakage&quot; and Rule 1b is &quot;Don't Break Dave.&quot;)&lt;/p&gt;
				</description>
			<pubDate>Sun, 29 Sep 2002 17:24:20 GMT</pubDate>
			<guid>http://scriptingnews.userland.com/backissues/2002/09/29#rule1</guid>

			</item>
		<item>
			<title>Really early morning no-coffee notes</title>
			<link>http://scriptingnews.userland.com/backissues/2002/09/29#reallyEarlyMorningNocoffeeNotes</link>
			<description>
				&lt;p&gt;One of the lessons I've learned in 47.4 years: When someone accuses you of a &lt;a href=&quot;http://www.dictionary.com/search?q=deceit&quot;&gt;deceit&lt;/a&gt;, there's a very good chance the accuser practices that form of deceit, and a reasonable chance that he or she is doing it as they point the finger. &lt;/p&gt;

				&lt;p&gt;&lt;a href=&quot;http://www.docuverse.com/blog/donpark/2002/09/28.html#a66&quot;&gt;Don Park&lt;/a&gt;: &quot;He poured a barrel full of pig urine all over the Korean Congress because he was pissed off about all the dirty politics going on.&quot;&lt;/p&gt;
				&lt;p&gt;&lt;a href=&quot;http://davenet.userland.com/1995/01/04/demoingsoftwareforfunprofi&quot;&gt;1/4/95&lt;/a&gt;: &quot;By the way, the person with the big problem is probably a competitor.&quot;&lt;/p&gt;

				&lt;p&gt;I've had a fair amount of experience in the last few years with what you might call standards work. XML-RPC, SOAP, RSS, OPML. Each has been different from the others. In all this work, the most positive experience was XML-RPC, and not just because of the technical excellence of the people involved. In the end, what matters more to me is &lt;a href=&quot;http://www.dictionary.com/search?q=collegiality&quot;&gt;collegiality&lt;/a&gt;. Working together, person to person, for the sheer pleasure of it, is even more satisfying than a good technical result. Now, getting both is the best, and while XML-RPC is not perfect, it's pretty good. I also believe that if you have collegiality, technical excellence follows as a natural outcome.&lt;/p&gt;
				&lt;p&gt;One more bit of philosophy. At my checkup earlier this week, one of the things my cardiologist asked was if I was experiencing any kind of intellectual dysfunction. In other words, did I lose any of my sharpness as a result of the surgery in June. I told him yes I had and thanked him for asking. In an amazing bit of synchronicity, the next day John Robb &lt;a href=&quot;http://jrobb.userland.com/2002/09/25.html#a2598&quot;&gt;located&lt;/a&gt; an article in New Scientist that said that scientists had found a way to prevent this from happening. I hadn't talked with John about my experience or the question the doctor asked. Yesterday I was telling the story to my friend Dave Jacobs. He said it's not a problem because I always had excess capacity in that area. Exactly right Big Dave and thanks for the vote of confidence.&lt;/p&gt;

				</description>
			<pubDate>Sun, 29 Sep 2002 11:13:10 GMT</pubDate>
			<guid>http://scriptingnews.userland.com/backissues/2002/09/29#reallyEarlyMorningNocoffeeNotes</guid>
			</item>
		</channel>
	</rss>
""")
