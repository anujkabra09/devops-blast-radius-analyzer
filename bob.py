"""
Mock BoB AI Client for testing purposes.
Replace this with the actual BoB SDK when available.
"""

class Client:
    """Mock BoB AI Client"""
    
    def __init__(self, api_key):
        """Initialize the BoB client with API key"""
        self.api_key = api_key
        print(f"✓ BoB Client initialized (API key: {api_key[:10]}...)")
    
    def generate(self, prompt):
        """Generate a response from the BoB AI model"""
        # Mock response for testing
        response = MockResponse()
        return response


class MockResponse:
    """Mock response object"""
    
    @property
    def text(self):
        """Return mock analysis text"""
        return """Change Type: Infrastructure Configuration Update

Risk Level: MEDIUM

What Could Break:
- Service availability during deployment
- Database connection pool exhaustion
- Increased memory usage on application servers
- Potential cache invalidation issues

Pre-Change Checks:
1. Verify current resource utilization is below 70%
2. Ensure backup and rollback procedures are tested
3. Check monitoring and alerting systems are operational
4. Validate configuration in staging environment
5. Review recent incident history for similar changes

Post-Change Monitoring:
1. Monitor application response times (first 15 minutes critical)
2. Track error rates and exception logs
3. Watch database connection pool metrics
4. Observe memory and CPU utilization trends
5. Check user-facing service health endpoints

Rollback Strategy:
1. Keep previous configuration version in version control
2. Maintain database backup taken immediately before change
3. Use feature flags to disable new functionality if needed
4. Prepare rollback script with estimated 5-minute execution time
5. Document rollback decision criteria and approval process

Note: This is a MOCK response for testing. Replace bob.py with actual BoB SDK."""

# Made with Bob
