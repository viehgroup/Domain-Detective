<h1 style="text-align:center;">Domain Detective</h1>
<p style="text-align:center;">A tool to enumerate subdomains, check for potential subdomain takeovers and scan for open ports on a given domain.</p>
<h2>Features</h2>
<ul>
  <li>Enumerate subdomains of a given domain using the socket library</li>
  <li>Check if a subdomain is takeoverable and if bypass is possible via HTTP verb tampering or custom header</li>
  <li>Scan for open ports on a given subdomain</li>
  <li>Hash the results of a scan to easily detect changes between scans</li>
  <li>Save the results of a scan to a file</li>
  <li>Load the results of a previous scan from a file</li>
</ul>
<h2>Requirements</h2>
<ul>
  <li>Python 3.x</li>
  <li>socket</li>
  <li>requests</li>
  <li>pandas</li>
  <li>hashlib</li>
</ul>
<h2>Installation</h2>
<p>Clone or download the repository and navigate to the directory in your terminal.</p>
<pre style="background-color:lightgray;">
<code>
$ git clone https://github.com/viehgroup/domain-detective.git
$ pip install -r requirements.txt
$ cd domain-detective
</code>
</pre>
<h2>Usage</h2>
<p>Run the following command in your terminal:</p>
<pre style="background-color:lightgray;">
<code>
$ python3 domain-detective.py
</code>
</pre>
<p>You will be prompted to enter the domain name. Once you have entered the domain name, the tool will enumerate subdomains, check for potential subdomain takeovers and scan for open ports.</p>
<h2>Output</h2>
<p>The results of each scan are saved to a file in a directory named after the domain. The directory will be created if it does not exist. The results are saved in a .csv file and can be loaded in a spreadsheet program such as Microsoft Excel or Google Sheets.</p>
<h2>Contribution</h2>
<p>Contributions to this tool are welcome. If you have an idea for a new feature or have found a bug, please open an issue on the GitHub repository.</p>
<h2>License</h2>
<p>This tool is licensed under the GPL 3.0 License. See the LICENSE file for more information.</p>
