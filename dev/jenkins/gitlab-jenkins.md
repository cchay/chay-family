Gitlab + Jenkins is now functional. We have a little bit of work to do to clean up the Jenkins script (add backup, rollback, etc.) but the connection both ways works and we have triggers working as well.

Couple things:
* In Jenkins
  1.      Polling must be enabled on the Jenkins job—but the poll frequency box should  be empty. This is required to make the hooks work
  2.      Repository URL is in format of git@gitlab.uscis.dhs.gov:did-it/cf_idcms.git
  3.      Credentials aren’t required
* In Gitlab
  1.      Web hook should be in the format of https://10.160.167.45/jenkins/git/notifyCommit?url=gitlab.uscis.dhs.gov:did-it/cf_idcms.git

Read thru this really quick: http://www.andyfrench.info/2015/03/automatically-triggering-jenkins-build.html
That’s what I found that helped me figure out the last 2 pieces. Interesting to know about the Git Polling Log. It’s right there but I never looked at it before. It was useful to debug though.