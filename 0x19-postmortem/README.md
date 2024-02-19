#0x19-postmortem
Postmortem: Slow API Response Times (January 15, 2024)
Issue Summary:
Duration: 3 hours (10:00 AM - 1:00 PM PST).
Impact: Our API experienced significantly slower response times, impacting 80% of users and causing delays in various application functionalities. No service outages occurred, but user experience was negatively affected.
Root Cause: Memory leak in the backend application logic, leading to resource exhaustion on the server.
Timeline:
10:00 AM PST: Monitoring alerts trigger for increased API response times and server memory usage.
10:15 AM PST: The on-call engineer investigates, initially suspecting database query performance issues.
10:30 AM PST: Analysis reveals no database bottlenecks. Server logs show increasing memory consumption by the backend application.
10:45 AM PST: The incident is escalated to the backend development team.
11:00 AM PST: Developers identify a memory leak in a recently deployed code update.
11:30 AM PST: A hotfix is developed and deployed, stopping the memory leak.
12:00 PM PST: Server memory usage stabilizes, and API response times gradually improve.
1:00 PM PST: Monitoring confirms normal API performance, and the incident is declared resolved.
Root Cause and Resolution:
The root cause of the slow response times was a memory leak in the backend application logic introduced by a recent code update. This leak caused the server to consume more and more memory, impacting its overall performance and leading to slower API responses.
The issue was resolved by deploying a hotfix that addressed the memory leak. This patch stopped the memory consumption and allowed the server to recover its performance.
Corrective and Preventative Measures:
Implement code reviews and static analysis tools to detect potential memory leaks in the future.![postmortem](https://github.com/Axcis380/alx-system_engineering-devops/assets/133226284/e2b1163b-9ae2-46c5-88b8-c587bfd567d0)

Run automated tests with simulated high loads to identify performance bottlenecks before deployment.
Improve monitoring and alerting to detect memory issues early and trigger faster response.
Invest in performance profiling tools to analyze resource usage and identify memory leaks efficiently.
By implementing these measures, we aim to prevent similar performance issues in the future and ensure a consistent and optimal user experience for our application.
