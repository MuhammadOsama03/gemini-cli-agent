# Security policy

## Tool boundary

Model output is untrusted input. Tool calls must be matched against an explicit allowlist, validated with typed arguments, and executed with bounded inputs and timeouts. A model response must never be interpreted as a shell command.

The calculator accepts only supported numeric operations. Search queries should have length limits, and returned web text must be treated as untrusted content rather than instructions.

## Secrets and privacy

Store the Gemini key only in the local environment file described by `.env.example`. Never log keys, authorization headers, or full exception payloads that may contain credentials. Avoid sending private or identifying information to search or model providers.

## Dependencies

Pin or review dependency upgrades, keep CI tests passing, and remove tools that are no longer used. Network failures and malformed tool arguments should fail safely without exposing stack traces to the user.

## Reporting

If you find a vulnerability, open a private security advisory in GitHub rather than a public issue. Include the affected version, impact, and minimal reproduction details without including real secrets.
