/**
 * House style: no em or en dashes in anything Kairos publishes. The prompt
 * asks for this, but models drift, so it is enforced here before a draft or
 * reply is stored. A spaced or bare dash between words becomes a comma; a
 * dash between numbers ("9–5") becomes a hyphen.
 */
export function plainPunctuation(text: string): string {
  return text
    .replace(/(\d)\s*[\u2013\u2014]\s*(\d)/g, '$1-$2')
    .replace(/\s*[\u2013\u2014]\s*/g, ', ')
    .replace(/,\s*([.,;:!?])/g, '$1')
    .replace(/^,\s*/gm, '')
    .replace(/ {2,}/g, ' ');
}
