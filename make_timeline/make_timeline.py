'''
source data looks like this, one per line:
2017-10-25 03:01:42,avwbmsgmp.ug
'''
inputfile = 'sample_dgas_firstseen.txt'
outputfile = 'sample_dgas_firstseen_timeline.html'

def write_append(filename, line):
    writefile = open(filename,'a')
    writefile.write(line)
    writefile.write('\n')
    writefile.close()

htmltop = """
<!DOCTYPE HTML>
<html>
<head>
  <title>Timeline basic demo</title>
  <script src="vis.min.js"></script>
  <link href="vis.min.css" rel="stylesheet" type="text/css" />

  <style type="text/css">
    body, html {
      font-family: sans-serif;
    }
  </style>
</head>
<body>
<div id="visualization"></div>
<script type="text/javascript">
  var container = document.getElementById('visualization');
  var data = ["""

htmlbottom = """];
  var options = {};
  var timeline = new vis.Timeline(container, data, options);
</script>
</body>
</html>"""

data = []
idnumber = 0
with open(inputfile,'r') as f:
	for line in f.read().split('\n'):
		l = line.split(',')
		try:
			dt = l[0]
			domain = l[1]
		except:
			continue
		idnumber +=1
		dataline = {'id':idnumber, 'content':domain,'start':dt}
		dataline = str(dataline)

		# dataline = "{"+"'id': "+str(idnumber)+", content: '"+domain+"', start: '"+dt+"'},"
		cleaneddataline = dataline.replace("'content'","content").replace("'start'","start").replace("'id'","id")
		data.append(cleaneddataline)

writefile = open(outputfile,'w')
write_append(outputfile,htmltop)
for i in data:
	write_append(outputfile,i + ",")
# htmlfinal = "{}{}{}".format(htmltop,data,htmlbottom)
write_append(outputfile,htmlbottom)