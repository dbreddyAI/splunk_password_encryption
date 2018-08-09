# splunk_password_encryption

## Example usage:

import splunkencrypt<br/>
mypassword='password'<br/><br/>
#Note: you really only need the first 16 bytes of your splunk.secret<br/>
splunk_secret='rBFTWO8gGZh0X7K0ugzGL7j.jeM.sbHxYEjWhK4zHiHC5QCVKF/byXopYr3TZHVANOplqC93K2EsieH/Z.mCTgVb32a4qeNoD/9zyWEs.8yEWhTExzR9rcmX4xaAnPId.GE3OkgKE6Bh4ploTP0KoVd8rHkudDjwrLgsGe82mCscIjZRQcOHFsUmtkBNe3zkaAiFmaYh1UK1kJC6VK/qTCw4KLSzff7N7LG0htvkjOdNRUpoFT.8pQZnBhVjl3'<br/><br/>
x=splunkencrypt.encrypt(mypassword,splunk_secret)<br/>
y=splunkencrypt.decrypt(x,splunk_secret[0:16])<br/><br/>
print x<br/>
print y<br/>


## Acknowledgments
TZK - reverse engineering the algorithm: http://maratto.blogspot.com/2016/03/reverse-engineering-splunk-password.html<br/>
Jurriaan Bremer - rc4 code: https://raw.githubusercontent.com/jbremer/rc4<br/>
