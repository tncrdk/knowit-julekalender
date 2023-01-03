@time begin
function Sieve(MaxLimit)
    AllNum = fill(false, MaxLimit)
    AllNum[2] = true
    AllNum[3] = true
    primes = []

    for i in 7:6:length(AllNum)
        AllNum[i] = true
        AllNum[i-2] = true
    end

    p = 6
    while p+1 <= MaxLimit
        if AllNum[p-1]
            push!(primes, p-1)
            for i in (p-1)^2:(p-1):MaxLimit
                AllNum[i] = false
            end
        end
        if AllNum[p+1]
            push!(primes, p+1)
            for i in (p+1)^2:(p+1):MaxLimit
                AllNum[i] = false
            end
        end
         p += 6
     end

     return AllNum
end

function PresentsToScrap(Top, AllNum)
    for i in Top:-1:0
        if AllNum[i]
            return i
        end
    end
end

function DeletingPresents(Limit)
    I = 0
    counter = 0
    primes = Sieve(Limit)

    while I <= Limit
        Searchlist = string(I, base = 10, pad = 7)
        if occursin("7", Searchlist)
            I += PresentsToScrap(I, primes) + 1
        else
            I += 1
            counter += 1
        end
    end

    return counter
end

println(DeletingPresents(5433000))

end
