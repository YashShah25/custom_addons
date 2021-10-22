Create a New Model named 'hr.referral.application' with following fields:
1. Name
2. Email
3. Referral Name - many2one (with hr.employee)
4. Degree - many2one (with hr.recruitment.degree)
5. Department - many2one (with hr.job)
6. Expected Salary
7. Summary
8. Expected joining Date


• This Should Contain Following Stages- Draft, Approved, Cancel

• Add a Button Named Approve. By Clicking this Button the Stage of the Record should be changed
to 'Approved'.

• Add a button named Create Application. This button should only be visible in Stage 'Approve'.


