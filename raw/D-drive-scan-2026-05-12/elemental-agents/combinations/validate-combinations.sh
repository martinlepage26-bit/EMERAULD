#!/usr/bin/env bash
set -euo pipefail

BASE_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DUAL_FILE="$BASE_DIR/dual-combinations.md"
TRIPLE_FILE="$BASE_DIR/triple-combinations.md"

fail() {
  echo "FAIL: $1" >&2
  exit 1
}

pass() {
  echo "PASS: $1"
}

require_file() {
  local file="$1"
  [[ -f "$file" ]] || fail "missing file: $file"
}

count_headings() {
  local file="$1"
  grep -c '^## ' "$file"
}

check_unique_dual_keys() {
  local dup_count
  dup_count="$(
    awk '
      /^## / {
        line=$0
        sub(/^## /, "", line)
        n=split(line, a, / \+ /)
        if (n!=2) {
          bad++
          next
        }
        x=a[1]; y=a[2]
        if (x<y) k=x"+"y; else k=y"+"x
        seen[k]++
      }
      END {
        dup=0
        for (k in seen) if (seen[k] > 1) dup++
        print dup
      }
    ' "$DUAL_FILE"
  )"
  [[ "$dup_count" == "0" ]] || fail "duplicate dual permutation keys detected ($dup_count)"
  pass "dual permutations are unique"
}

check_unique_triple_keys() {
  local dup_count
  dup_count="$(
    awk '
      function sort3(a,b,c,  t){
        if (a>b){t=a;a=b;b=t}
        if (b>c){t=b;b=c;c=t}
        if (a>b){t=a;a=b;b=t}
        return a"+"b"+"c
      }
      /^## / {
        line=$0
        sub(/^## /, "", line)
        n=split(line, a, / \+ /)
        if (n!=3) {
          bad++
          next
        }
        k=sort3(a[1], a[2], a[3])
        seen[k]++
      }
      END {
        dup=0
        for (k in seen) if (seen[k] > 1) dup++
        print dup
      }
    ' "$TRIPLE_FILE"
  )"
  [[ "$dup_count" == "0" ]] || fail "duplicate triple permutation keys detected ($dup_count)"
  pass "triple permutations are unique"
}

check_required_fields() {
  local file="$1"
  local expected
  expected="$(count_headings "$file")"
  local field count
  for field in \
    "Natural manifestation:" \
    "Operational function:" \
    "Autonomous automation behavior:" \
    "Risk or imbalance:" \
    "Recommended lead agent:"
  do
    count="$(grep -c "^$field" "$file")"
    [[ "$count" == "$expected" ]] || fail "$file missing required field count for '$field' ($count/$expected)"
  done
  if [[ "$file" == "$TRIPLE_FILE" ]]; then
    count="$(grep -c '^Supporting agents:' "$file")"
    [[ "$count" == "$expected" ]] || fail "$file missing required field count for 'Supporting agents:' ($count/$expected)"
  fi
  pass "$(basename "$file") required fields complete"
}

check_unique_triple_manifestations() {
  local dups
  dups="$(
    grep '^Natural manifestation:' "$TRIPLE_FILE" \
      | sed 's/^Natural manifestation: //' \
      | sort \
      | uniq -cd \
      | sed 's/^ *//'
  )"
  [[ -z "$dups" ]] || fail "duplicate triple manifestations detected:\n$dups"
  pass "triple manifestation labels are unique"
}

check_no_manifestation_stutter() {
  local bad
  bad="$(
    awk '
      /^## / {
        heading = $0
        sub(/^## /, "", heading)
      }
      /^Natural manifestation:/ {
        m = $0
        sub(/^Natural manifestation: /, "", m)
        if (m ~ /Source Field Source Field|Ether Field Ether Field|Field Field/) {
          print heading " -> " m
        }
      }
    ' "$DUAL_FILE" "$TRIPLE_FILE"
  )"
  [[ -z "$bad" ]] || fail "manifestation stutter detected:\n$bad"
  pass "manifestation labels avoid repeated token stutter"
}

check_escalation_lead_rule() {
  local bad
  bad="$(
    awk '
      /^## / {
        heading=$0
        sub(/^## /, "", heading)
      }
      /^Recommended lead agent: / {
        lead=$0
        sub(/^Recommended lead agent: /, "", lead)
        has_non_escalation=0
        split(heading, parts, / \+ /)
        for (i in parts) {
          p=parts[i]
          if (p != "Spirit" && p != "Chi" && p != "Akasha") {
            has_non_escalation=1
          }
        }
        if ((lead=="Spirit" || lead=="Chi" || lead=="Akasha") && has_non_escalation==1) {
          print heading " -> " lead
        }
      }
    ' "$DUAL_FILE" "$TRIPLE_FILE"
  )"
  [[ -z "$bad" ]] || fail "escalation lead used as routine peer:\n$bad"
  pass "Spirit/Chi/Akasha lead rule passes"
}

check_akasha_field_keyword() {
  local bad_count
  bad_count="$(
    awk '
      /^## / {
        heading=$0
        sub(/^## /, "", heading)
        has_akasha = (heading ~ /Akasha/)
      }
      /^Natural manifestation:/ {
        if (!has_akasha && $0 ~ /Ether Field/) {
          bad++
        }
      }
      END { print bad+0 }
    ' "$DUAL_FILE" "$TRIPLE_FILE"
  )"
  [[ "$bad_count" == "0" ]] || fail "Akasha filler naming detected outside Akasha combinations ($bad_count)"
  pass "Akasha naming rule passes"
}

main() {
  require_file "$DUAL_FILE"
  require_file "$TRIPLE_FILE"

  local dual_count triple_count
  dual_count="$(count_headings "$DUAL_FILE")"
  triple_count="$(count_headings "$TRIPLE_FILE")"
  [[ "$dual_count" == "45" ]] || fail "expected 45 dual combinations, found $dual_count"
  [[ "$triple_count" == "120" ]] || fail "expected 120 triple combinations, found $triple_count"
  pass "combination counts are correct (dual=$dual_count, triple=$triple_count)"

  check_unique_dual_keys
  check_unique_triple_keys
  check_required_fields "$DUAL_FILE"
  check_required_fields "$TRIPLE_FILE"
  check_unique_triple_manifestations
  check_no_manifestation_stutter
  check_escalation_lead_rule
  check_akasha_field_keyword

  echo "PASS: all combination checks succeeded"
}

main "$@"
