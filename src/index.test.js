import { describe, it } from 'node:test';
import assert from 'node:assert';
import { hello, getVersion } from './index.js';

describe('My CLI Tool', () => {
  it('should return hello message', () => {
    const result = hello();
    assert.strictEqual(result, 'Hello, World!');
  });

  it('should return hello with custom name', () => {
    const result = hello('GitHub');
    assert.strictEqual(result, 'Hello, GitHub!');
  });

  it('should return version', () => {
    const version = getVersion();
    assert.strictEqual(version, '1.0.0');
  });
});
