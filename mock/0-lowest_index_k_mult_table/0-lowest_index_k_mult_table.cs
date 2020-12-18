using System;
using System.Linq;

namespace _0_lowest_index_k_mult_table
{
    public static class Module {
        
        public static object minValue(object indexSplit, object m, object n, object k) {
            var count = 0;
            foreach (var i in Enumerable.Range(1, m + 1 - 1)) {
                count += min(indexSplit / i, n);
            }
            return count >= k;
        }
        
        public static object getIndexK(object m, object n, object k) {
            var floor = 1;
            var peak = m * n;
            while (floor < peak) {
                var middle = (floor + peak) / 2;
                if (!minValue(middle, m, n, k)) {
                    floor = middle + 1;
                } else {
                    peak = middle;
                }
            }
            return floor;
        }
    }
}
