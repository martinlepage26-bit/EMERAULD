import { describe, it, expect } from 'vitest';
import { plainPunctuation } from '../src/lib/text';

describe('plainPunctuation', () => {
  it.each([
    ['It follows your data to whoever they subcontract to — hosting, models.', 'It follows your data to whoever they subcontract to, hosting, models.'],
    ['That is by design—built to look effortless.', 'That is by design, built to look effortless.'],
    ['Open 9–5, Monday to Friday.', 'Open 9-5, Monday to Friday.'],
    ['Nobody quotes that part — .', 'Nobody quotes that part.'],
    ['— Starts with a dash.', 'Starts with a dash.'],
    ['No dashes here, all good.', 'No dashes here, all good.'],
  ])('%s', (input, expected) => {
    expect(plainPunctuation(input)).toBe(expected);
    expect(plainPunctuation(input)).not.toMatch(/[–—]/);
  });
});
