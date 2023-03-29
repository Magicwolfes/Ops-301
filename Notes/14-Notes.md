# What is Group Policy and What Role Does It Play in Data Security


## What role does Group Policy play in Windows Active Directory?
> A Group Policy Object (GPO) is a group of settings that are created using the Microsoft Management Console (MMC) Group Policy Editor. GPOs can be associated with single or numerous Active Directory containers, including sites, domains, or organizational units (OUs). The MMC allows users to create GPOs that define registry-based policies, security options, software installation, and much more.

Active Directory applies GPOs in the same, logical order; local policies, site policies, domain policies and OU policies.

## Name and describe different ways GPOs can benefit security.
- Password Policy: Many organizations are operating with relaxed password policies, with many users often having passwords set to never expire. Passwords that aren’t regularly rotated, are too simple or use common passphrases are at risk of being hacked through brute force. GPOs can be used to establish password length, complexity and other requirements.
- Systems Management: GPOs can be used to simplify tasks that are at best mundane and at worst critically time-consuming. You can save yourself hours and hours of time configuring the environment of new users and computers joining your domain by using GPOs to apply a standardized, universal one.
- Health Checking: GPOs can be used to deploy software updates and system patches to ensure your environment is healthy and up to date against the latest security threats.

## How can the acronym “LSDOU” help you figure out which policies are in effect?
The order in which GPOs are processed affects what settings are applied to the computer and user. The order that GPOs are processed is known as LSDOU, which stands for local, site, domain, and organizational unit. The local computer policy is the first to be processed, followed by the site level to domain AD policies, then finally into organization units. If there happen to be conflicting policies in LSDOU, the last applied policies win out.