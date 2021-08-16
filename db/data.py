import pymongo
from access_tfbot import MONGO_TOKEN
client = pymongo.MongoClient(MONGO_TOKEN)
db = client.test
db = client["tfBot_database"]
collection = db["bot_fase1_db"]

collection.insert_one({'word_searched': 'technological', 'tweet_found': 'technological bubble - tesla will fuel this bubble. excitement of all people to profit on ai plus extra low interest rate.', 'tweet_found_tokens': ['technological', 'bubble', 'tesla', 'will', 'fuel', 'this', 'bubble', '.', 'excitement', 'of', 'all', 'people', 'to', 'profit', 'on', 'ai', 'plus', 'extra', 'low', 'interest', 'rate', '.'], 'twt_found_ordered_tokens': ['.', 'ai', 'bubble', 'excitement', 'extra', 'fuel', 'interest', 'low', 'people', 'plus', 'profit', 'rate', 'technological', 'tesla'], 'random_word_in_trigram': [('technological', 'bubble', 'tesla')], 'txt_sended': 'We can thus see that one can have technology without the technological understanding of being, so it be comes clear that the technological understanding of being can be dissociated from techno', 'txt_sended_tokens': ['We', 'thus', 'see', 'one', 'technology', 'without', 'technological', 'understanding', ',', 'comes', 'clear', 'technological', 'understanding', 'dissociated', 'techno'], 'word_in_twt_trigrams': [('technology', 'without', 'technological')]})
collection.insert_one({'word_searched': 'device', 'tweet_found': '@balconybody i see this so often from you i’m gonna  take your mobile device', 'tweet_found_tokens': ['@', 'balconybody', 'i', 'see', 'this', 'so', 'often', 'from', 'you', 'i', 'm', 'gonna', 'take', 'your', 'mobile', 'device'], 'twt_found_ordered_tokens': ['@', 'balconybody', 'device', 'gonna', 'mobile', 'often', 'see', 'take'], 'random_word_in_trigram': [('take', 'mobile', 'device')], 'txt_sended': 'DimiS (aka Sexophone or Love Machine, 1972) is a device that generates sounds', 'txt_sended_tokens': ['DimiS', '(', 'aka', 'Sexophone', 'Love', 'Machine', ',', '1972', ')', 'device', 'generates', 'sounds'], 'word_in_twt_trigrams': [('1972', ')', 'device')]})
collection.insert_one({'word_searched': 'device', 'tweet_found': "@fixd_app why is it so hard to talk to someone from customer service. i have a device that doesn't work &amp; i even si… https://t.co/6b4gofqxbd", 'tweet_found_tokens': ['@', 'fixd_app', 'why', 'is', 'it', 'so', 'hard', 'to', 'talk', 'to', 'someone', 'from', 'customer', 'service', '.', 'i', 'have', 'a', 'device', 'that', 'doesn', "'", 't', 'work', 'amp', ';', 'i', 'even', 'si', 'https', ':', 't', '.', 'co', '6b4gofqxbd'], 'twt_found_ordered_tokens': ["'", '.', '6b4gofqxbd', ':', ';', '@', 'amp', 'co', 'customer', 'device', 'even', 'fixd_app', 'hard', 'https', 'service', 'si', 'someone', 'talk', 'work'], 'random_word_in_trigram': [('service', '.', 'device'), ('.', 'device', "'"), ('device', "'", 'work')], 'txt_sended': 'DimiS (aka Sexophone or Love Machine, 1972) is a device that generates sounds through the skin contact of four performers w', 'txt_sended_tokens': ['DimiS', '(', 'aka', 'Sexophone', 'Love', 'Machine', ',', '1972', ')', 'device', 'generates', 'sounds', 'skin', 'contact', 'four', 'performers', 'w'], 'word_in_twt_trigrams': [('1972', ')', 'device')]})
collection.insert_one({'word_searched': 'tool', 'tweet_found': '#homebakery #bakerslife cream 38 pcs baking pastry tool pastry tools bakeware confectionery bags nozzles confection… https://t.co/mfikbep8vr', 'tweet_found_tokens': ['homebakery', 'bakerslife', 'cream', '38', 'pcs', 'baking', 'pastry', 'tool', 'pastry', 'tools', 'bakeware', 'confectionery', 'bags', 'nozzles', 'confection', 'https', ':', 't', '.', 'co', 'mfikbep8vr'], 'twt_found_ordered_tokens': ['.', '38', ':', 'bags', 'bakerslife', 'bakeware', 'baking', 'co', 'confection', 'confectionery', 'cream', 'homebakery', 'https', 'mfikbep8vr', 'nozzles', 'pastry', 'pcs', 'tool', 'tools'], 'random_word_in_trigram': [('baking', 'pastry', 'tool'), ('pastry', 'tool', 'pastry'), ('tool', 'pastry', 'tools')], 'txt_sended': 'We know that backpropagation algorithms are a datamining tool used for classification, clustering, and', 'txt_sended_tokens': ['We', 'know', 'backpropagation', 'algorithms', 'datamining', 'tool', 'used', 'classification', ',', 'clustering', ','], 'word_in_twt_trigrams': [('algorithms', 'datamining', 'tool')]})
collection.insert_one({'word_searched': 'technological', 'tweet_found': 'rt @celestinebee: a vaccine passport makes no sense until you realise none of this is about a virus. it’s about finding a way to link peopl…', 'tweet_found_tokens': ['rt', '@', 'celestinebee', ':', 'a', 'vaccine', 'passport', 'makes', 'no', 'sense', 'until', 'you', 'realise', 'none', 'of', 'this', 'is', 'about', 'a', 'virus', '.', 'it', 's', 'about', 'finding', 'a', 'way', 'to', 'link', 'peopl'], 'twt_found_ordered_tokens': ['.', ':', '@', 'celestinebee', 'finding', 'link', 'makes', 'none', 'passport', 'peopl', 'realise', 'rt', 'sense', 'vaccine', 'virus', 'way'], 'random_word_in_trigram': [], 'txt_sended': 'We can thus see that one can have technology without the technological understanding of being, so it be comes clear that the technological understanding of being can be dissociated from technological ', 'txt_sended_tokens': ['We', 'thus', 'see', 'one', 'technology', 'without', 'technological', 'understanding', ',', 'comes', 'clear', 'technological', 'understanding', 'dissociated', 'technological'], 'word_in_twt_trigrams': [('technology', 'without', 'technological')]})
collection.insert_one({'word_searched': 'informational', 'tweet_found': 'rt @singh_harjiv: effective feedback:\n\n✅focuses on critical aspects of the task( similar to intrinsic) \n✅informational or motivational \n✅tr…', 'tweet_found_tokens': ['rt', '@', 'singh_harjiv', ':', 'effective', 'feedback', ':', 'focuses', 'on', 'critical', 'aspects', 'of', 'the', 'task', '(', 'similar', 'to', 'intrinsic', ')', 'informational', 'or', 'motivational', 'tr'], 'twt_found_ordered_tokens': ['(', ')', ':', '@', 'aspects', 'critical', 'effective', 'feedback', 'focuses', 'informational', 'intrinsic', 'motivational', 'rt', 'similar', 'singh_harjiv', 'task', 'tr'], 'random_word_in_trigram': [('intrinsic', ')', 'informational'), (')', 'informational', 'motivational'), ('informational', 'motivational', 'tr')], 'txt_sended': 'Individuation takes place when three conditions are met, namely material, energetic, and informational, which are not yet individuated being', 'txt_sended_tokens': ['Individuation', 'takes', 'place', 'three', 'conditions', 'met', ',', 'namely', 'material', ',', 'energetic', ',', 'informational', ',', 'yet', 'individuated'], 'word_in_twt_trigrams': [('energetic', ',', 'informational')]})
collection.insert_one({'word_searched': 'technology', 'tweet_found': 'rt @truthabtchina: china was extremely excited to show off new technology they recently stole from the americans when this happened.\n\nafter…', 'tweet_found_tokens': ['rt', '@', 'truthabtchina', ':', 'china', 'was', 'extremely', 'excited', 'to', 'show', 'off', 'new', 'technology', 'they', 'recently', 'stole', 'from', 'the', 'americans', 'when', 'this', 'happened', '.', 'after'], 'twt_found_ordered_tokens': ['.', ':', '@', 'americans', 'china', 'excited', 'extremely', 'happened', 'new', 'recently', 'rt', 'show', 'stole', 'technology', 'truthabtchina'], 'random_word_in_trigram': [('show', 'new', 'technology'), ('new', 'technology', 'recently'), ('technology', 'recently', 'stole')], 'txt_sended': 'Whether this will happen, I don’t know! However I see in the essence of technology the first emergence of a very deep mystery (Geheimnis) which I cal', 'txt_sended_tokens': ['Whether', 'happen', ',', 'I', '’', 'know', '!', 'However', 'I', 'see', 'essence', 'technology', 'first', 'emergence', 'deep', 'mystery', '(', 'Geheimnis', ')', 'I', 'cal'], 'word_in_twt_trigrams': [('see', 'essence', 'technology')]})
collection.insert_one({'word_searched': 'technical', 'tweet_found': "@gtrxman it's not just that dogecoin started as a joke: it has serious foundational and technical flaws that forecl… https://t.co/gnaclqvgvo", 'tweet_found_tokens': ['@', 'gtrxman', 'it', "'", 's', 'not', 'just', 'that', 'dogecoin', 'started', 'as', 'a', 'joke', ':', 'it', 'has', 'serious', 'foundational', 'and', 'technical', 'flaws', 'that', 'forecl', 'https', ':', 't', '.', 'co', 'gnaclqvgvo'], 'twt_found_ordered_tokens': ["'", '.', ':', '@', 'co', 'dogecoin', 'flaws', 'forecl', 'foundational', 'gnaclqvgvo', 'gtrxman', 'https', 'joke', 'serious', 'started', 'technical'], 'random_word_in_trigram': [('serious', 'foundational', 'technical'), ('foundational', 'technical', 'flaws'), ('technical', 'flaws', 'forecl')], 'txt_sended': 'The technical rhythm, according to LeroiGourhan, transforms “untamed nature into instruments of ', 'txt_sended_tokens': ['The', 'technical', 'rhythm', ',', 'according', 'LeroiGourhan', ',', 'transforms', '“', 'untamed', 'nature', 'instruments'], 'word_in_twt_trigrams': [('The', 'technical', 'rhythm')]})
collection.insert_one({'word_searched': 'information', 'tweet_found': 'rt @ambaamonye: please repost and reach out to henry county police if you have any information about her https://t.co/2akogifeef', 'tweet_found_tokens': ['rt', '@', 'ambaamonye', ':', 'please', 'repost', 'and', 'reach', 'out', 'to', 'henry', 'county', 'police', 'if', 'you', 'have', 'any', 'information', 'about', 'her', 'https', ':', 't', '.', 'co', '2akogifeef'], 'twt_found_ordered_tokens': ['.', '2akogifeef', ':', '@', 'ambaamonye', 'co', 'county', 'henry', 'https', 'information', 'please', 'police', 'reach', 'repost', 'rt'], 'random_word_in_trigram': [('county', 'police', 'information'), ('police', 'information', 'https'), ('information', 'https', ':')], 'txt_sended': 'If\n\n80 hui\n\nresearch in phenomenology 47 (2017) 60–84\n\nwe now understand “missing” as the information that triggers a transformation to come, then in this transformatio', 'txt_sended_tokens': ['If', '80', 'hui', 'research', 'phenomenology', '47', '(', '2017', ')', '60–84', 'understand', '“', 'missing', '”', 'information', 'triggers', 'transformation', 'come', ',', 'transformatio'], 'word_in_twt_trigrams': [('missing', '”', 'information')]})
collection.insert_one({'word_searched': 'tech', 'tweet_found': 'rt @isob_ell: i will not rest until i see chopper bullying tech #thebadbatch #badbatch https://t.co/igqjjhrtzw', 'tweet_found_tokens': ['rt', '@', 'isob_ell', ':', 'i', 'will', 'not', 'rest', 'until', 'i', 'see', 'chopper', 'bullying', 'tech', 'thebadbatch', 'badbatch', 'https', ':', 't', '.', 'co', 'igqjjhrtzw'], 'twt_found_ordered_tokens': ['.', ':', '@', 'badbatch', 'bullying', 'chopper', 'co', 'https', 'igqjjhrtzw', 'isob_ell', 'rest', 'rt', 'see', 'tech', 'thebadbatch'], 'random_word_in_trigram': [('chopper', 'bullying', 'tech'), ('bullying', 'tech', 'thebadbatch'), ('tech', 'thebadbatch', 'badbatch')], 'txt_sended': 'This transcendental instrumentality opens the question of the relation between doing and thinking which is at the core of the critique of tech', 'txt_sended_tokens': ['This', 'transcendental', 'instrumentality', 'opens', 'question', 'relation', 'thinking', 'core', 'critique', 'tech'], 'word_in_twt_trigrams': [('core', 'critique', 'tech')]})
collection.insert_one({'word_searched': 'technological', 'tweet_found': 'rt @hyken: with today’s technological capabilities, why should a customer have to reach out for help to begin with? in many instances, comp…', 'tweet_found_tokens': ['rt', '@', 'hyken', ':', 'with', 'today', 's', 'technological', 'capabilities', ',', 'why', 'should', 'a', 'customer', 'have', 'to', 'reach', 'out', 'for', 'help', 'to', 'begin', 'with', '?', 'in', 'many', 'instances', ',', 'comp'], 'twt_found_ordered_tokens': [',', ':', '?', '@', 'begin', 'capabilities', 'comp', 'customer', 'help', 'hyken', 'instances', 'many', 'reach', 'rt', 'technological', 'today'], 'random_word_in_trigram': [(':', 'today', 'technological'), ('today', 'technological', 'capabilities'), ('technological', 'capabilities', ',')], 'txt_sended': 'In other words, this computational indifference to binary problemsolving coincides with a new imperative: technological decisionism, which values making a clear decision quickly more than it does making the co', 'txt_sended_tokens': ['In', 'words', ',', 'computational', 'indifference', 'binary', 'problemsolving', 'coincides', 'new', 'imperative', ':', 'technological', 'decisionism', ',', 'values', 'making', 'clear', 'decision', 'quickly', 'making', 'co'], 'word_in_twt_trigrams': [('imperative', ':', 'technological')]})
collection.insert_one({'word_searched': 'technological', 'tweet_found': 'rt @omkar_raii: #msmes can play a transformational role in bolstering indian economy by driving technological innovations, empowering #star…', 'tweet_found_tokens': ['rt', '@', 'omkar_raii', ':', 'msmes', 'can', 'play', 'a', 'transformational', 'role', 'in', 'bolstering', 'indian', 'economy', 'by', 'driving', 'technological', 'innovations', ',', 'empowering', 'star'], 'twt_found_ordered_tokens': [',', ':', '@', 'bolstering', 'driving', 'economy', 'empowering', 'indian', 'innovations', 'msmes', 'omkar_raii', 'play', 'role', 'rt', 'star', 'technological', 'transformational'], 'random_word_in_trigram': [('economy', 'driving', 'technological'), ('driving', 'technological', 'innovations'), ('technological', 'innovations', ',')], 'txt_sended': '\nLuciana Parisi\n\nReprogramming Decisionism\n\nComputational indifference to binary problemsolving coincides with a new imperative: technological decisionism, which values m', 'txt_sended_tokens': ['Luciana', 'Parisi', 'Reprogramming', 'Decisionism', 'Computational', 'indifference', 'binary', 'problemsolving', 'coincides', 'new', 'imperative', ':', 'technological', 'decisionism', ',', 'values'], 'word_in_twt_trigrams': [('imperative', ':', 'technological')]})
collection.insert_one({'word_searched': 'algorithm', 'tweet_found': "rt @nevsoc: it's important to recognize that not all socialists are alike. after months of analyzing socialists online i have completed an…", 'tweet_found_tokens': ['rt', '@', 'nevsoc', ':', 'it', "'", 's', 'important', 'to', 'recognize', 'that', 'not', 'all', 'socialists', 'are', 'alike', '.', 'after', 'months', 'of', 'analyzing', 'socialists', 'online', 'i', 'have', 'completed', 'an'], 'twt_found_ordered_tokens': ["'", '.', ':', '@', 'alike', 'analyzing', 'completed', 'important', 'months', 'nevsoc', 'online', 'recognize', 'rt', 'socialists'], 'random_word_in_trigram': [], 'txt_sended': '\nFor instance, unlike recommendation algorithms, the RankBrain interpreter algorithm', 'txt_sended_tokens': ['For', 'instance', ',', 'unlike', 'recommendation', 'algorithms', ',', 'RankBrain', 'interpreter', 'algorithm'], 'word_in_twt_trigrams': [('RankBrain', 'interpreter', 'algorithm')]})
collection.insert_one({'word_searched': 'technological', 'tweet_found': '@jnyhne all this here technological stuff is sure tough to learn.', 'tweet_found_tokens': ['@', 'jnyhne', 'all', 'this', 'here', 'technological', 'stuff', 'is', 'sure', 'tough', 'to', 'learn', '.'], 'twt_found_ordered_tokens': ['.', '@', 'jnyhne', 'learn', 'stuff', 'sure', 'technological', 'tough'], 'random_word_in_trigram': [('@', 'jnyhne', 'technological'), ('jnyhne', 'technological', 'stuff'), ('technological', 'stuff', 'sure')], 'txt_sended': 'In other words, this computational indifference to binary problemsolving coincides with a new imperative: technological decisionism, which values making a ', 'txt_sended_tokens': ['In', 'words', ',', 'computational', 'indifference', 'binary', 'problemsolving', 'coincides', 'new', 'imperative', ':', 'technological', 'decisionism', ',', 'values', 'making'], 'word_in_twt_trigrams': [('imperative', ':', 'technological')]})
collection.insert_one({'word_searched': 'instrument', 'tweet_found': '1837 drawing by 🇯🇲 artist; i. m. belisario, of a john canoe [joonkanoo] band accompanying masqueraders. the drum ha… https://t.co/rcy6fbqidt', 'tweet_found_tokens': ['1837', 'drawing', 'by', 'artist', ';', 'i', '.', 'm', '.', 'belisario', ',', 'of', 'a', 'john', 'canoe', '[', 'joonkanoo', ']', 'band', 'accompanying', 'masqueraders', '.', 'the', 'drum', 'ha', 'https', ':', 't', '.', 'co', 'rcy6fbqidt'], 'twt_found_ordered_tokens': [',', '.', '1837', ':', ';', '[', ']', 'accompanying', 'artist', 'band', 'belisario', 'canoe', 'co', 'drawing', 'drum', 'ha', 'https', 'john', 'joonkanoo', 'masqueraders', 'rcy6fbqidt'], 'random_word_in_trigram': [], 'txt_sended': 'Similarly, the conception of the mean or instrument of governance—that is, information technology—is left as a black box that has no aims (it is in itself a mindless, nonconscious automata) unless these are political', 'txt_sended_tokens': ['Similarly', ',', 'conception', 'mean', 'instrument', 'governance—that', ',', 'information', 'technology—is', 'left', 'black', 'box', 'aims', '(', 'mindless', ',', 'nonconscious', 'automata', ')', 'unless', 'political'], 'word_in_twt_trigrams': [('conception', 'mean', 'instrument')]})
collection.insert_one({'word_searched': 'technological', 'tweet_found': 'rt @jackvardan: there are a number of technological investments that could be featured in the third offset in order to counter future asymm…', 'tweet_found_tokens': ['rt', '@', 'jackvardan', ':', 'there', 'are', 'a', 'number', 'of', 'technological', 'investments', 'that', 'could', 'be', 'featured', 'in', 'the', 'third', 'offset', 'in', 'order', 'to', 'counter', 'future', 'asymm'], 'twt_found_ordered_tokens': [':', '@', 'asymm', 'could', 'counter', 'featured', 'future', 'investments', 'jackvardan', 'number', 'offset', 'order', 'rt', 'technological', 'third'], 'random_word_in_trigram': [(':', 'number', 'technological'), ('number', 'technological', 'investments'), ('technological', 'investments', 'could')], 'txt_sended': '\nLuciana Parisi\n\nReprogramming Decisionism\n\nComputational indifference to binary problemsolving coincides with a new imperative: technological decisionism, ', 'txt_sended_tokens': ['Luciana', 'Parisi', 'Reprogramming', 'Decisionism', 'Computational', 'indifference', 'binary', 'problemsolving', 'coincides', 'new', 'imperative', ':', 'technological', 'decisionism', ','], 'word_in_twt_trigrams': [('imperative', ':', 'technological')]})
collection.insert_one({'word_searched': 'tech', 'tweet_found': 'we seems to be in a "tech startup bubble" like earlier dot com bubble. will burst and then revive again. proper cap… https://t.co/aj8zoplxyf', 'tweet_found_tokens': ['we', 'seems', 'to', 'be', 'in', 'a', '"', 'tech', 'startup', 'bubble', '"', 'like', 'earlier', 'dot', 'com', 'bubble', '.', 'will', 'burst', 'and', 'then', 'revive', 'again', '.', 'proper', 'cap', 'https', ':', 't', '.', 'co', 'aj8zoplxyf'], 'twt_found_ordered_tokens': ['"', '.', ':', 'aj8zoplxyf', 'bubble', 'burst', 'cap', 'co', 'com', 'dot', 'earlier', 'https', 'like', 'proper', 'revive', 'seems', 'startup', 'tech'], 'random_word_in_trigram': [('seems', '"', 'tech'), ('"', 'tech', 'startup'), ('tech', 'startup', 'bubble')], 'txt_sended': 'Photo: NASA/David Roy\n\nThese questions require us to focus not on how intelligent machines represent knowledge as an aggregation of datafacts; we must also embark on a materialist inquiry into the tech', 'txt_sended_tokens': ['Photo', ':', 'NASA/David', 'Roy', 'These', 'questions', 'require', 'us', 'focus', 'intelligent', 'machines', 'represent', 'knowledge', 'aggregation', 'datafacts', ';', 'must', 'also', 'embark', 'materialist', 'inquiry', 'tech'], 'word_in_twt_trigrams': [('materialist', 'inquiry', 'tech')]})
collection.insert_one({'word_searched': 'technology', 'tweet_found': '"imagine being a dumbass pigeon, no technology, no society, look at you out in the rain you fucking eejit." - @greatscottlp', 'tweet_found_tokens': ['"', 'imagine', 'being', 'a', 'dumbass', 'pigeon', ',', 'no', 'technology', ',', 'no', 'society', ',', 'look', 'at', 'you', 'out', 'in', 'the', 'rain', 'you', 'fucking', 'eejit', '.', '"', '@', 'greatscottlp'], 'twt_found_ordered_tokens': ['"', ',', '.', '@', 'dumbass', 'eejit', 'fucking', 'greatscottlp', 'imagine', 'look', 'pigeon', 'rain', 'society', 'technology'], 'random_word_in_trigram': [('pigeon', ',', 'technology'), (',', 'technology', ','), ('technology', ',', 'society')], 'txt_sended': 'As these forms of automated intelligence have entered the social culture of communication, they have also become central to a critical theory of technology that has incessantly warned us agai', 'txt_sended_tokens': ['As', 'forms', 'automated', 'intelligence', 'entered', 'social', 'culture', 'communication', ',', 'also', 'become', 'central', 'critical', 'theory', 'technology', 'incessantly', 'warned', 'us', 'agai'], 'word_in_twt_trigrams': [('critical', 'theory', 'technology')]})
collection.insert_one({'word_searched': 'technology', 'tweet_found': 'rt @ummjackson: after years of studying it, i believe that cryptocurrency is an inherently right-wing, hyper-capitalistic technology built…', 'tweet_found_tokens': ['rt', '@', 'ummjackson', ':', 'after', 'years', 'of', 'studying', 'it', ',', 'i', 'believe', 'that', 'cryptocurrency', 'is', 'an', 'inherently', 'right-wing', ',', 'hyper-capitalistic', 'technology', 'built'], 'twt_found_ordered_tokens': [',', ':', '@', 'believe', 'built', 'cryptocurrency', 'hyper-capitalistic', 'inherently', 'right-wing', 'rt', 'studying', 'technology', 'ummjackson', 'years'], 'random_word_in_trigram': [(',', 'hyper-capitalistic', 'technology'), ('hyper-capitalistic', 'technology', 'built')], 'txt_sended': 'Compared with poetry, technology is mor', 'txt_sended_tokens': ['Compared', 'poetry', ',', 'technology', 'mor'], 'word_in_twt_trigrams': [('poetry', ',', 'technology')]})
