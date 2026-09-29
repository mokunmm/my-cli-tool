/**
 * My CLI Tool
 * Main entry point for programmatic usage
 */

export function hello(name = 'World') {
  return `Hello, ${name}!`;
}

export function getVersion() {
  return '1.0.0';
}
