# What is an Active Directory

## What exactly is “Active Directory” and are the key services it provides?
Active Directory (AD) is Microsoft’s directory and identity management service for Windows domain networks

- A schema that defines the classes of objects and attributes contained in the directory.
- A global catalog that contains detailed information about every object in the directory.
- A query and index mechanism that allows users, administrators, and applications to efficiently find directory information.
- A replication service that disseminates directory data across the network.

## What are the differences between a domain, forest, and tree in Active Directory?
- A *domain* is a collection of objects (e.g. users, devices) that share the same Active Directory database. A domain is identified by a DNS name like company.com.
- A *tree* is a collection of one or more domains with a contiguous namespace (they have a common DNS root name like marketing.company.com, engineering.company.com, and sales.company.com).
A *forest* is a collection of one or more trees that share a common schema, global catalog, and directory configuration—but aren’t part of a contiguous namespace. The forest typically serves as the security boundary for an enterprise network.

## How can objects (e.g. users, devices) within a domain be grouped?
> Objects within a domain can be grouped into organizational units (OUs) to simplify administration and policy management. Administrators can create arbitrary organizational units to mirror functional, geographical, or business structures, and then apply group policies to OUs to simplify administration. OUs also make it easier to delegate control over resources to various administrators.

## Explain the benefits of Active Directory, as you would to a family member.
- Security – Active Directory helps businesses improve security by controlling access to network resources.
- Extensibility – companies can easily organize Active Directory data to align with their organizational structure and business needs.
- Simplicity – administrators can centrally manage user identities and access privileges across the enterprise, helping businesses simplify management and reduce operations expenses.
- Resiliency – Active Directory supports redundant components and data replication to enable high availability and business continuity.