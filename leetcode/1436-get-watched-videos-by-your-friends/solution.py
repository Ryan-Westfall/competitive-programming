class Solution:
    def watchedVideosByFriends(self, watchedVideos: List[List[str]], friends: List[List[int]], id: int, level: int) -> List[str]:
        videoCounter = Counter()
        visited = set({id})
        queue = deque([id])
        curLevel = 0
        
        while queue:
            for _ in range(len(queue)):
                index = queue.popleft()
                if curLevel == level:
                    for video in watchedVideos[index]:
                        videoCounter[video] += 1
                    continue
                for friend in friends[index]:
                    if friend not in visited:
                        visited.add(friend)
                        queue.append(friend)
            curLevel += 1

        return [item for item, _ in sorted(videoCounter.items(), key=lambda x: (x[1], x[0]))]


        

                    


                