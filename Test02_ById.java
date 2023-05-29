package edu.uic.cs474.s23.a3;

import org.junit.Assert;
import org.junit.Test;

import java.util.*;

public class Test02_ById {

    @Test
    public void testRandom() {
        Random r = new Random();
        List<HasId> data = new ArrayList<>();

        for (int i = 0 ; i < 10 ; i++) {
            while(true) {
                JustId h = new JustId(r.nextInt());
                if (!data.contains(h)){
                    data.add(h);
                    break;
                }
            }
        }

        Map<Integer, HasId> expected = new HashMap<>();
        for(HasId d : data)
            expected.put(d.getId(), d);

        StreamProcessor processor = Main.getProcessor();
        Assert.assertEquals(expected, processor.problem2(data));
    }

    static class JustId implements HasId{
        int id;

        public JustId(int i){
            this.id = i;
        }
        @Override
        public int getId() {
            return this.id;
        }

        @Override
        public boolean equals(Object obj) {
            /*if(obj instanceof JustId)*/ return ((JustId) obj).id == this.id;
            //else return false;
        }
    }
}
