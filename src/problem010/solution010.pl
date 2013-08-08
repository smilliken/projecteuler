my $max = 2000000;
my $sum = 0;
my @nums = (0 .. $max);
@nums[1] = 0;
foreach my $n (@nums) {
    my $i = 2;
    $sum += @nums[$n];
    while ($n > 1 && $i * $n < $max) {
        $nums[($i++) * $n] = 0;
    }
}
print $sum, "\n";
