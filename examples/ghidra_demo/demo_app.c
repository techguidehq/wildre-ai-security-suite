#include <stdio.h>
#include <stdint.h>
#include <string.h>

/* Benign training fixture: no network, filesystem writes, or persistence. */
static uint32_t checksum(const unsigned char *data, size_t length) {
    uint32_t value = 2166136261u;
    for (size_t i = 0; i < length; i++) {
        value ^= data[i];
        value *= 16777619u;
    }
    return value;
}

int main(void) {
    const unsigned char marker[] = "WILDRE_DEMO_MARKER";
    printf("WildRE training demo: %s\n", marker);
    printf("Checksum: %u\n", checksum(marker, strlen((const char *)marker)));
    return 0;
}
